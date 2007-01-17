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

from hotkeys import *

def printKeysOldStyle(keylist, output):
               
    for nr in keylist:
        if not linuxkeycodes.has_key(nr) or nr == 240:
            continue
        linuxname = linuxkeycodes[nr]
        xkeycode = xkeycodes.symbolFromLinux(nr)
        xkeysym = linux2x.linux2x(linuxname)
        if not xkeysym or not xkeycode:
            output.write('// ')
        else:
            output.write('   ')
        if xkeycode is None:
            xkeycode = '<XXXX>'
        key = "key %6s { [ %s ] };" % (xkeycode, xkeysym)
        output.write(key)
        if len(key) < 42:
            output.write(" " * (42 - len(key)))
        output.write("// KEY_%s\n" % linuxname)

def printKeys(keylist, output):
    for nr in keylist:
        ok = True
        linuxname = linuxkeycodes[nr]
        xkeysym = linux2x.linux2x(linuxname)
        if not xkeysym:
            ok = False
        if not ok:
            output.write('// ')
        else:
            output.write('   ')
        output.write("key %14s { [ %s ] };\n" % ('<%s>' % linuxname, xkeysym))

def printLinux(output):
    keylist = range(112, 117) + range(127, 179) + \
              range(181, 183) + range(200, 256)
    output.write("partial alphanumeric_keys\n")
    output.write('xkb_symbols "linux" {\n')
    printKeysOldStyle(keylist, output)
    output.write("};\n\n")

    output.write("partial alphanumeric_keys\n")
    output.write('xkb_symbols "evdev" {\n')
    output.write('    include "linux"\n')
    printKeysOldStyle(range(0x160, 0x1d0) + range(0x1f1, 0x1f9), output)
    output.write("};\n\n")                

def printJp(output):
    keylist = range(89,96) + range(118, 118) + range(122, 124)
    output.write("partial alphanumeric_keys\n")
    output.write('xkb_symbols "jp" {\n')
    printKeys(keylist, output)
    output.write("};\n\n")


def main():
    if len(sys.argv) != 2:
        print """
USAGE xkbd_linux_symbols.py FILE
\t- for standard out
\twrite xkbd symbol tables for kbd and evdev driver X11 keyboard driver
"""
        sys.exit(1)
    if sys.argv[1] == "-":
        output = sys.stdout
    else:
        output = open(sys.argv[1], "w")

    printLinux(output)
    #printJp(output)

main()
