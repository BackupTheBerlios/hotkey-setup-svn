#!/usr/bin/python

from hotkeys import *
import re

class XkbdKeyboard(Keyboard):
    def __init__(self, name, brand='', model=''):
        if not brand and not model:
            brand, model = self._splitName(name)
        Keyboard.__init__(self, name, brand , model)
            
debug = 0

class XkbParser:

    keyboard_re = re.compile('^xkb_symbols "(.*)" {$')
    key_re = re.compile('key\s*(<[0-9A-Za-z]+>)\s*\{\s*\[\s*(\S+)\s'
                        '(,\s(\S+))?\s*\]\s*\};')

    def __init__(self, filename='/usr/share/X11/xkb/symbols/inet'):
        self.filename = filename

    def parse(self):
        kbds = []
        in_keyboard = False
        for line in open(self.filename):
            comment = line.find('//')
            if comment != -1:
                line = line[:comment]
            line = line.strip()
            if in_keyboard:
                if line == "};":
                    in_keyboard = False
                    continue
                m = self.key_re.match(line)
                if m:
                    keyname = m.group(1)
                    try:
                        scancode = xkeycodes.scancode(keyname)
                    except KeyError:
                        if debug: print "XXXX", keyname
                        continue
                    keysym = m.group(2)
                    keyboard.addKey(scancode, xkeysym=keysym)
                    #print keyname, keysym
                    
            else:
                if line == 'partial alphanumeric_keys':
                    continue
                m =  self.keyboard_re.match(line)
                if m:
                    keyboard = XkbdKeyboard(m.group(1))
                    in_keyboard = True
                    kbds.append(keyboard)
        return kbds

def getKeyboards(file='/usr/share/X11/xkb/symbols/inet'):
    parser = XkbParser(file)
    return [kb for kb in parser.parse() if kb.valid]
    

def main():
    kbds = getKeyboards()
    for kb in kbds:
        print kb.name, kb.brand, kb.model
        for key in kb.keys:
            print "\t", key

if __name__ == '__main__':
    main()
