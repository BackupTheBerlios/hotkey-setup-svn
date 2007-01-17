#!/usr/bin/python
import os, sys, re, xml.parsers.expat
from elementtree.ElementTree import parse
from hotkeys import *

class KeytouchKeyboard(Keyboard):

    mapping = {
        'Camera' : 'CAMERA',
        'VOlUMEDOWN' : 'VOLUMEDOWN',
        'Mute' : 'MUTE',
        }

    def __init__(self, filename):
        Keyboard.__init__(self, name=filename)
        self.name = filename
        try:
            tree = parse(filename)
            root = tree.getroot()
            keys = root.find('key-list')
            self.brand = root.find('./keyboard-info/keyboard-name/manufacturer').text
            self.model = root.find('./keyboard-info/keyboard-name/model').text
            # XXX extract more info
        except xml.parsers.expat.ExpatError, e:
            self.valid = False
            print e
            print self.filename, " ",

        for key in keys:
            try:
                scancode = int(key.find('scancode').text)
                keyname = key.find('keycode').text
                if keyname in self.mapping:
                    keyname = self.mapping[keyname]
                elif keyname not in linuxkeys:
                    print "KKK", keyname
                    continue
                if scancode == 0:
                    continue
                    # scancode = linuxkeys[keyname]
                    #print keyname, scancode, xkeycodes.groups["basic"].get(scancode)
            except (AttributeError, KeyError), e:
                #print "EEE", e
                continue
            self.addKey(scancode, linuxname=keyname)
        self._checkKeys()
        self.valid = bool(self.keys)

def getKeyboards(file='keytouch'):
    kbds = []
    for filename in os.listdir(file):
        kbd = KeytouchKeyboard(file + filename)     
        if kbd.valid:
            kbds.append(kbd)
    return kbds

