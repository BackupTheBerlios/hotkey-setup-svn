#!/usr/bin/python

## Copyright (C) 2007 Red Hat, Inc.
## Copyright (C) 2007 Florian Festi <ffesti@redhat.com>

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sys, cStringIO, os.path, optparse
from readers import lineak, hotkeysetup, keytouch, xkbd

def statistic(keyboards):
    keys = 0
    empty_keys = 0
    for kb in keyboards:
        #kb.fixKeys()
        keys += len(kb.keys)
        for scancode, linuxname, xkeysym in kb.keys:
            if not linuxname and not xkeysym:
                empty_keys += 1
    print len(keyboards), "keyboards;", keys, "keys;", empty_keys, "empty keys"

def matchKbs(keyboards):
    kbs = {}
    for kb in keyboards:
        keys = [k[0] for k in kb.keys]
        keys.sort()
        kbs.setdefault(tuple(keys), []).append(kb)
    for keys, l in kbs.iteritems():
        if len(l) > 1 and keys:
            print keys, 
            for kb in l:
                print kb.name,
            print

def writeXmodmap(keyboards):
    for kb in keyboards:
        if not kb.keys: continue
        kb.xmodmap()


def checkDiffs(keyboards, output=sys.stdout):
    i = 0
    #for kb in keyboards:
    #    kb.fixKeys()
    equals = {}
    redundant = 0
    non_redundant_keyboards = set(keyboards)
    for nr, kb1 in enumerate(keyboards):
        if not kb1.keys:
            redundant += 1
            non_redundant_keyboards.discard(kb1)
            continue
        duplicate = False
        for kb2 in keyboards:
            if not kb2.keys: continue
            if kb1 is kb2: continue
            
            diff1, diff2 = kb1.diff(kb2)
            if kb1.name == kb2.name:                
                output.write("XXX same names %s %r %r\n" %
                             (kb1.name, kb1, kb2))
            if diff1 < 1:
                duplicate = True
                i += 1
            if diff1 == 0  and diff2 == 0:
                if kb2 in non_redundant_keyboards:
                    non_redundant_keyboards.discard(kb2)
            elif diff1 == 0:
                non_redundant_keyboards.discard(kb1)
        if duplicate:
            redundant += 1
            output.write("%3i %s\n" % (redundant, kb1.name))
    output.write(
        "==================================================================\n")
    for nr, kb in enumerate(non_redundant_keyboards):
        output.write("%3i %s\n" % (nr, kb.name))
    output.write("Redundant %s\n" % redundant)
    return non_redundant_keyboards


def findKeys(keyboards, *keys):
    for kb in keyboards:
        for scancode, linuxname, xkeysym in kb.keys:
            for key in keys:
                if linuxname == key or xkeysym == key:
                    print key, kb.name, kb

def writeKeymaps(keyboards, directory=None):
    kbds = [(kb.getQuotedName(), kb) for kb in keyboards]
    kbds.sort()
    output = sys.stdout
    for name, kb in kbds:
        print name,  "(%s)" % kb.__class__.__name__.replace('Keyboard', '')
        if directory:
            output = open(os.path.join(directory, name), 'w')
        kb.keymap(output = output, comments=True)
        if directory:
            output.close()
    
def main_old():
    keyboards = []
    for source in (
        keytouch,
        # lineak,
        #xkbd,
        hotkeysetup,
        ):
        keyboards.extend(source.getKeyboards())
    keyboards = checkDiffs(keyboards, cStringIO.StringIO())
    #findKeys(keyboards, 'CONNECT', 'CYCLEWINDOWS', 'DIRECTION', 'FILE',
    #         'MACRO', 'SPORT')
    #matchKbs(keyboards)
    #writeXmodmap(keyboards)
    #writeKeymaps(keyboards, '/home/str/ffesti/hotkeys/codefiles')
    statistic(keyboards)


def main():
    parser = optparse.OptionParser("%prog [options] TARGETDIR")
    parser.add_option("-k", "--keytouch", dest="keytouch", action="store_true",
                      help="Include settings from keytouch")
    parser.add_option("-l", "--lineak", dest="lineak", action="store_true",
                      help="Include settings from lineak")
    parser.add_option("--hotkey-setup", dest="hotkeysetup",
                      action="store_true",
                      help="Include settings from hotkey-setup")
    parser.add_option("-x", "--xkbd", dest="xkbd", action="store_true",
                      help="Include settings from xkbd")
    (options, args) = parser.parse_args()

    if len(args) != 1 or not os.path.isdir(args[0]):
        parser.error("You must give an existing target directory")

    sources = []
    if options.keytouch:
        sources.append(keytouch)
    if options.lineak:
        sources.append(lineak)
    if options.hotkeysetup:
        sources.append(hotkeysetup)
    if options.xkbd:
        sources.append(xkbd)

    keyboards = []
    for source in sources:
        keyboards.extend(source.getKeyboards())

    writeKeymaps(keyboards, args[0])
    statistic(keyboards)

main()
