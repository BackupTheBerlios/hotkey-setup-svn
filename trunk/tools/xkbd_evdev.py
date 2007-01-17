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

import sys
from hotkeys import *

def printKeycodes(keylist, output):
               
    for nr in keylist:
        ok = True
        try:
            linuxname = linuxkeycodes[nr]
        except KeyError:
            continue
        output.write('%20s = %d;\n' % ('<%s>' % linuxname, nr + 8))

def printKeycodesOldstyle(keylist, output):
               
    for nr in keylist:
        # linux name
        if not linuxkeycodes.has_key(nr) or nr == 240: # KEY_UNKNOWN 
            continue
        linuxname = linuxkeycodes[nr]

        xkeycode = xkeycodes.symbolFromLinux(nr)
        if xkeycode is None:
            output.write('//  ')
            xkeycode = '<XXXX>'
        else:
            output.write('    ')
        output.write('%6s = %d; // %s\n' % (xkeycode, nr + 8, linuxname))
        
def writeKeycodes(output):
    output.write('default xkb_keycodes "evdev" {\n')
    output.write('    minimum = 8;\n')
    output.write('    maximum = 459;\n\n')
    printKeycodesOldstyle(range(1, 0x1d0) + range(0x1f1, 0x1f9), output)
    #printKeycodesOldstyle(range(1, 84) + range(86, 89) + range(96, 112) +
    #                      range(117, 120) + [121] + range(183, 195),
    #                      output)
    #printKeycodesOldStyle(
    #    [85] + range(89,96) +  range(112, 117) + range(122, 183) +
    #    range(200, 237) + range(0x160, 0x1c4), output)
    output.write('};\n\n')


def main():
    if len(sys.argv) != 2:
        print """
USAGE xkbd_evdev.py FILE
\t- for standard out
\twrite a xkbd keycodes table for the evdev X11 keyboard driver
"""
        sys.exit(1)
    if sys.argv[1] == "-":
        output = sys.stdout
    else:
        output = open(sys.argv[1], "w")

    writeKeycodes(output)


main()
