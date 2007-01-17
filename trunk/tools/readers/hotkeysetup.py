#!/usr/bin/python
from hotkeys import *
import os, re

class HotkeySetupKeyboard(Keyboard):

    mapping = {
        'LIGHT' : 'F19',
        'VIDEOOUT' : 'F20',
        'ROTATESCREEN' : 'F21',
        'VIDEOMODECYCLE' : 'F22',
        'PRESENTATION' : 'F23',
        'BATTERY' : 236,
    }
        

    line_re = re.compile(r'^\s*setkeycodes\s+([0-9a-fA-F]+)\s+\$KEY_(\S+)')

    def __init__(self, filename):
        Keyboard.__init__(self, filename)
        name = os.path.basename(filename)
        if name.endswith('.hk'):
            name = name[:-3]
        name = name .split('-', 1)
        if len(name) == 2:
            self.brand, self.model = name
        elif len(name) == 1:
            self.brand, self.model = name[0], ''
        else:
            raise ValueError, "Irregular finelname: %s " % filename

        for line in open(filename):
            m = self.line_re.match(line)
            if m:
                try:
                    scancode = int(m.group(1)[-2:], 16) # decode last byte
                except ValueError:
                    continue
                if len(m.group(1)) == 4 and m.group(1)[:2] == 'e0':
                    scancode += 128
                elif len(m.group(1)) != 2:
                    continue
                linuxname=m.group(2)
                if linuxname in self.mapping:
                    linuxname = self.mapping[linuxname]
                self.addKey(scancode, linuxname=linuxname) 
        self._checkKeys()

def getKeyboards(
    file='../hotkey-setup/'):
    keyboards = []
    for filename in os.listdir(file):
        if filename.endswith('.hk') and filename != 'atkbd.hk':
            kb = HotkeySetupKeyboard(file + filename)
            if kb.valid:
                keyboards.append(kb)
    return keyboards
