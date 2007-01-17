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

import re, sys, string, os.path
from pprint import pprint

path = os.path.dirname(__file__)

class ReverseDict(dict):
    def __init__(self, forward_mapping):
        for key, value in forward_mapping.iteritems():
            self[value] = key

# ======================================================================
# === Linux Key codes ===
# ======================================================================

class LinuxKeyCodes(dict):
    """mapping name -> keycode"""

    line_re = re.compile(r'#define\s*KEY_(\S+)\s+(0x[0-9A-Fa-f]+|\d+)\s*')

    def __init__(self, filename='/usr/include/linux/input.h'):
        self.filename = filename
        self.parse(filename)

    def parse(self, filename):
        for line in open(filename):
            m = self.line_re.match(line)
            if m:                
                code = m.group(2)
                if code.startswith('0x'):
                    code = int(code[2:], 16)
                elif code.startswith('0') and code!='0':
                    code = int(code[1:], 8)
                else:
                    code = int(code)
                self[m.group(1)] = code


LinuxKey2Scan = [
      0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,
     16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
     48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
     64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
     80, 81, 82, 83, 84,118, 86, 87, 88,115,120,119,121,112,123, 92,
    284,285,309,  0,312, 91,327,328,329,331,333,335,336,337,338,339,
    367,288,302,304,350, 89,334,326,267,126,268,269,125,347,348,349,
    360,261,262,263,268,376,100,101,321,316,373,286,289,102,351,355,
    103,104,105,275,287,279,306,106,274,107,294,364,358,363,362,361,
    291,108,381,281,290,272,292,305,280, 99,112,257,258,359,113,114,
    264,117,271,374,379,265,266, 93, 94, 95, 85,259,375,260, 90,116,
    377,109,111,277,278,282,283,295,296,297,299,300,301,293,303,307,
    308,310,313,314,315,317,318,319,320,357,322,323,324,325,276,330,
    332,340,365,342,343,344,345,346,356,270,341,368,369,370,371,372 ]

LinuxKey2X = [
      0,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
     24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
     40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
     56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
     72, 73, 74, 75, 76, 77, 76, 79, 80, 81, 82, 83, 84, 85, 86, 87,
     88, 89, 90, 91,111,221, 94, 95, 96,211,128,127,129,208,131,126,
    108,109,112,111,113,181, 97, 98, 99,100,102,103,104,105,106,107,
    239,160,174,176,222,157,123,110,139,134,209,210,133,115,116,117,
    232,133,134,135,140,248,191,192,122,188,245,158,161,193,223,227,
    198,199,200,147,159,151,178,201,146,203,166,236,230,235,234,233,
    163,204,253,153,162,144,164,177,152,190,208,129,130,231,209,210,
    136,220,143,246,251,137,138,182,183,184, 93,184,247,132,170,219,
    249,205,207,149,150,154,155,167,168,169,171,172,173,165,175,179,
    180,  0,185,186,187,118,119,120,121,229,194,195,196,197,148,202,
    101,212,237,214,215,216,217,218,228,142,213,240,241,242,243,244,
      0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0
]

# ==============================================================
# === X Key symbols ===
#===============================================================

class XKeysymDB(dict):
    """mapping name -> code"""

    def __init__(self, filename='/usr/share/X11/XKeysymDB'):
        self.comments = {} # offer same interface as XKeySyms
        for nr, line in enumerate(open(filename)):
            if not line or line[0] == '!':
                continue
            line = line.split()
            if not line:
                continue
            if len(line) != 2 or line[1][0] != ':':
                raise ParseError, "%r" % line
            self[line[0]] = line[1][1:]

class XKeysymDef(dict):
    """mapping name -> code"""

    define_re = r'^\#define XK_([a-zA-Z_0-9]+)\s+0x([0-9a-f]+)\s*'
    line_res = (
        re.compile(define_re + r'\/\* U+([0-9A-F]{4,6}) (.*) \*\/\s*$'),
            # /* U+0000 Comment */
        re.compile(define_re + r'\/\*\(U+([0-9A-F]{4,6}) (.*)\)\*\/\s*$'),
            # /* (U+0000 Comment */
        re.compile(define_re + r'(\/\*\s*(.*)\s*\*\/)?\s*$'),)
            # /* Comment /*

    def __init__(self, filename='/usr/include/X11/keysymdef.h'):
        self.comments = {}
        self.extensions = {} # name -> linuxname
        for line in open(filename):
            for line_re in self.line_res:
                m = line_re.match(line)
                if not m:
                    continue
                scancode = int(m.group(2), 16)
                self[m.group(1)] = scancode
                if m.lastindex>2:
                    comment = m.group(m.lastindex)
                    if comment:
                        self.comments[m.group(1)] = comment

    def addExtensions(self, filename):
        regex = re.compile(
            r'^\#define XK_([a-zA-Z_0-9]+)\s+(\/\*\s*(\S+).*\*\/)?\s*$')
        for line in open(filename):
            m = regex.match(line)
            if not m: continue
            self[m.group(1)] = None
            self.extensions[m.group(1)] = m.group(3)
                
            

class XKeysyms(dict):
    def __init__(self):
        self.comments = {}
        self.xkeysymdb = XKeysymDB()
        self.xkeysyms = XKeysymDef()
        self.xkeysyms.addExtensions(path + '/xkeys.txt')
        self.update(self.xkeysymdb)
        self.update(self.xkeysyms)
        self.comments.update(self.xkeysyms.comments)

# =====================================================================
# === X keycodes ===
# =====================================================================

class XKeycodes:
    """scancode -> symbolic name"""

    new_section_re = re.compile(r'(default)?\s*xkb_keycodes\s"([^"]*)"\s*\{')
    end_section_re = re.compile(r'\s*\};')
    statement_re = re.compile(r'(\S+)\s*=\s*(\d+)\s*;')
    alias_re = re.compile(r'alias\s+(\S+)\s*=\s*(\S+)\s*;')

    def __init__(self, filename='/usr/share/X11/xkb/keycodes/xfree86'):
        self._groups_sym2code = {}
        self._groups_code2sym = {}

        section_name = None
        for nr , line in enumerate(open(filename)):
            comment = line.find('//')
            if comment != -1:
                line = line[:comment]
            line = line.strip()
            if not line: continue
            m = self.new_section_re.match(line)
            if m:
                if section_name:
                    raise ValueError, "Line %i: %r" % (nr, line)
                section_name = m.group(2) # XXX default
                sym2code = {}
                code2sym = {}
                self._groups_code2sym[section_name] = code2sym
                self._groups_sym2code[section_name] = sym2code
                continue
            m = self.statement_re.match(line)
            if m:
                scancode = int(m.group(2))
                sym2code[m.group(1)] = scancode

                if self._cmpSymbols(m.group(1), code2sym.get(scancode)):
                    code2sym[scancode] = m.group(1)
                continue
            m = self.alias_re.match(line)
            if m:
                if m.group(2) in sym2code:
                    scancode = sym2code[m.group(2)]
                    sym2code[m.group(1)] = scancode
                    if self._cmpSymbols(m.group(1), code2sym.get(scancode)):
                        code2sym[scancode] = m.group(1)
                
            m = self.end_section_re.match(line)
            if m:
                section_name = None

    def _cmpSymbols(self, sym1, sym2):
        if not sym2:
            return True
        if re.match(r'[IK][0-9A-F]{2}', sym1):
            return True
        return False
                
    def scancode(self, symbol, group='basic'):
        return self._groups_sym2code[group][symbol]

    def symbol(self, keycode, group='basic'):
        return self._groups_code2sym[group][keycode]

    def symbolFromLinux(self, linuxkeycode):
        if linuxkeycode > 255:
            return '<X%03X>' % linuxkeycode

        scancode = LinuxKey2X[linuxkeycode]
        if not scancode:
            return '<X%2X>' % linuxkeycode
        
        if scancode > 255:
            scancode = scancode & 0xFF | 0x80
        try:
            return self.symbol(scancode)
        except:
            try:
                return self.symbol(scancode, 'xfree86')
            except:
                return '<X%2X>' % linuxkeycode
        
# =====================================================================
# === Linux <-> X key mappings ===
# =====================================================================

class Linux2X:

    def __init__(self):
        self._linux2x = {
            # Hacks
            'CONNECT' : '', # NEEDED 
            'CYCLEWINDOWS' : '', # NEEDED 
            'FASTFORWARD' : '', # NEEDED 
            'DELETEFILE' : '',
            'MACRO' : '', # NEEDED 
            'SPORT' : '', # NEEDED 
            'QUESTION': '', # XXX 
            'CLOSECD' : 'XF86Eject',
            'ISO' : '',
            'ALTERASE' : 'BackSpace', # Erase-Eaze Key
            'KBDILLUMDOWN' : '', # XXX 
            'KBDILLUMTOGGLE' : '',
            'KBDILLUMUP' : '', # XXX

            # one by one / unresolved
            '102ND' : '',
            'AB' : '',
            'ADDRESSBOOK' : '',
            'AGAIN' : 'Redo',
            'ANGLE' : '',
            'ARCHIVE' : '',
            'AUDIO' : '',
            'AUX' : '',
            'BACK' : 'XF86Back',
            'BASSBOOST' : '',
            'BATTERY' : '',
            'BLUE' : '',
            'BLUETOOTH' : '',
            'BOOKMARKS' : 'XF86Favorites',
            'BREAK' : 'Break',
            'BRIGHTNESSDOWN' : 'SunVideoLowerBrightness',
            'BRIGHTNESSUP' : 'SunVideoRaiseBrightness',
            'BRL_DOT1' : 'braille_dot_1',
            'BRL_DOT2' : 'braille_dot_2',
            'BRL_DOT3' : 'braille_dot_3',
            'BRL_DOT4' : 'braille_dot_4',
            'BRL_DOT5' : 'braille_dot_5',
            'BRL_DOT6' : 'braille_dot_6',
            'BRL_DOT7' : 'braille_dot_7',
            'BRL_DOT8' : 'braille_dot_8',
            'CALC' : 'XF86Calculator',
            'CALENDAR': 'XF86Calendar',
            'CAMERA' : 'XF86WebCam',
            'CANCEL' : 'Cancel',
            'CAPSLOCK' : 'Caps_Lock',
            'CD': 'XF86CD',
            'CHANNEL' : '',
            'CHANNELDOWN' : '',
            'CHANNELUP' : '',
            'CHAT' : 'XF86Messenger',
            'CLEAR': 'Clear',
            'CLOSE' : 'XF86Close',
            'COFFEE' : 'XF86ScreenSaver',
            'COMPOSE' : 'Multi_key', # maps to <MENU> -> Menu ???
            'COMPUTER' : 'XF86MyComputer',
            'CONFIG' : 'XF86Option',
            'COPY' : 'XF86Copy',
            'CUT' : 'XF86Cut',
            'DATABASE' : '',
            'DEL_EOL' : '',
            'DEL_EOS' : '',
            'DELETE' : 'Delete',
            'DEL_LINE' : '',
            'DIGITS' : '',
            'DIRECTION' : 'XF86RotateWindows',
            'DIRECTORY' : '',
            'DOCUMENTS' : 'XF86Documents',
            'DOWN' : 'Down',
            'DVD' : '',
            'EDIT' : 'apEdit',
            'EDITOR' : '',
            'EJECTCD' : 'XF86Eject',
            'EJECTCLOSECD' : 'XF86Eject',
            'EMAIL' : 'XF86Mail',
            'END' : 'End',
            'EPG' : '',
            'EQUAL' : 'equal',
            'EXIT' : 'Cancel',
            'FAVORITES': 'XF86Favorites',
            'FILE' : 'XF86Explorer',
            'FINANCE' : 'XF86Finance',
            'FIND' : 'Find',
            'FIRST' : '',
            'FN' : '',
            'FN_B' : '',
            'FN_D' : '',
            'FN_E' : '',
            'FN_ESC' : '',
            'FN_F' : '',
            'FN_F1' : '',
            'FN_F10' : '',
            'FN_F11' : '',
            'FN_F12' : '',
            'FN_F2' : '',
            'FN_F3' : '',
            'FN_F4' : '',
            'FN_F5' : '',
            'FN_F6' : '',
            'FN_F7' : '',
            'FN_F8' : '',
            'FN_F9' : '',
            'FN_S' : '',
            'FORWARDMAIL' : 'XF86MailForward',
            'FORWARD' : 'XF86Forward',
            'FRONT' : 'SunFront',
            'GAMES' : 'XF86Game',
            'GOTO' : 'XF86Go',
            'GRAPHICSEDITOR' : '',
            'GREEN' : '',
            'HANGEUL' : 'Hangul',
            'HANJA' : 'Hangul_Hanja',
            'HELP' : 'Help',
            'HENKAN' : 'Henkan',
            'HIRAGANA' : 'Hiragana',
            'HOME' : 'Home',
            'HOMEPAGE' : 'XF86HomePage',
            'HP' : 'XF86HomePage',
            'INFO' : 'Help', # XXX
            'INSERT' : 'Insert',
            'INS_LINE' : '',
            'KATAKANAHIRAGANA' : 'prolongedsound',
            'KATAKANA' : 'Katakana',
            'KEYBOARD' : '',
            'KPASTERISK' : 'KP_Multiply',
            'KPJPCOMMA' : 'kana_comma',
            'KPLEFTPAREN' : 'parenleft',
            'KPPLUSMINUS' : 'plusminus',
            'KPRIGHTPAREN' : 'parenright',
            'LANGUAGE' : '',
            'LAST' : '',
            'LEFT' : 'Left',
            'LEFTMETA' : 'Meta_L',
            'LINEFEED' : 'Linefeed',
            'LIST' : '',
            'MAIL' : 'XF86Mail',
            'MEDIA' : 'XF86AudioMedia',
            'MEMO': 'XF86Memo',
            'MENU' : 'XF86MenuKB',
            'MESSENGER' : 'XF86Messenger',
            'MHP' : '',
            'MINUS' : 'minus',
            'MODE' : '',
            'MOVE' : 'apMove',
            'MP3' : 'XF86AudioMedia',
            'MSDOS' : 'apShell',
            'MUHENKAN' : 'Muhenkan',
            'MUTE' : 'XF86AudioMute',
            'NEW' : 'XF86New',
            'NEWS' : 'XF86News',
            'NEXT': 'Next',
            'NEXTSONG' : 'XF86AudioNext',
            'NUMLOCK' : 'Num_Lock',
            'OK' : '',
            'OPEN' : 'XF86Open',
            'OPTION': 'XF86Option',
            'PASTE' : 'XF86Paste',
            'PAUSECD' : 'XF86AudioPause',
            'PAUSE' : 'Pause',
            'PC' : '',
            'PHONE' : 'XF86Phone',
            'PLAYCD' : 'XF86CD', # play???
            'PLAYER' : '',
            'PLAYPAUSE' : 'XF86AudioPlay',
            'PLAY' : 'XF86AudioPlay',
            'POWER2' : '', # remote control C-
            'POWER' : 'XF86PowerOff',
            'PRESENTATION' : '',
            'PREVIOUS' : 'Prior',
            'PREVIOUSSONG' : 'XF86AudioPrev',
            'PRINT' : 'Print',
            'PROG1' : 'XF86Launch0',
            'PROG2' : 'XF86Launch1',
            'PROG3' : 'XF86Launch2',
            'PROG4' : 'XF86Launch3',
            'PROGRAM' : 'XF86LaunchA', # XXX
            'PROPS' : 'XF86Option',
            'PVR' : '',
            'RADIO' : '',
            'RECORD' : 'XF86AudioRecord',
            'RED' : '',
            'REDO' : 'Redo',
            'REFRESH' : 'XF86Refresh',
            'REPLY' : 'XF86Reply',
            'RESERVED' : '',
            'RESTART' : '',
            'REWIND' : 'XF86AudioRewind',
            'RIGHTMETA' : 'Meta_R',
            'RIGHT' : 'Right',
            'RO' : 'Romaji', # ???
            'SAT' : '',
            'SAT2' : '',
            'SAVE' : 'XF86Save',
            'SCREEN' : '',
            'SCROLLDOWN' : 'XF86ScrollDown',
            'SCROLLUP' : 'XF86ScrollUp',
            'SCROLLLOCK' : 'Scroll_Lock',
            'SEARCH' : 'XF86Search',
            'SELECT': 'Select',
            'SENDFILE' : 'XF86Send', # XXX
            'SEND' : 'XF86Send',
            'SETUP' : 'XF86Option',
            'SHOP' : 'XF86Shop',
            'SHUFFLE' : '',
            'SLASH' : 'slash',
            'SLEEP' : 'XF86Sleep',
            'SLOW' : 'SlowKeys_Enable',
            'SOUND' : 'XF86AudioMedia',
            'SPREADSHEET' : 'XF86Excel',
            'STOPCD' : 'XF86AudioStop',
            'STOP' : 'XF86Stop',
            'SUBTITLE' : '',
            'SUSPEND' : 'XF86Sleep',
            'SWITCHVIDEOMODE' : 'XF86_Next_VMode',
            'SYSRQ' : 'Sys_Req',
            'TAB' : 'Tab',
            'TAPE' : '',
            'TEEN' : '',
            'TEXT' : '',
            'TIME' : '',
            'TITLE' : '',
            'TUNER' : '',
            'TV' : '',
            'TV2' : '',
            'TWEN' : '',
            'UNDO' : 'Undo',
            'UNKNOWN' : '',
            'UP' : 'Up',
            'VCR' : '',
            'VCR2' : '',
            'VENDOR' : 'XF86VendorHome',
            'VIDEO': 'XF86Video',
            'VOICEMAIL' : '',
            'VOLUMEDOWN' : 'XF86AudioLowerVolume',
            'VOLUMEUP' : 'XF86AudioRaiseVolume',
            'WAKEUP' : 'XF86WakeUp',
            'WLAN' : '',
            'WORDPROCESSOR' : 'XF86Word',
            'WWW' : 'XF86WWW',
            'XFER': 'XF86Xfer',
            'YELLOW' : '',
            'YEN' : 'yen',
            'ZENKAKUHANKAKU' : 'Zenkaku_Hankaku',
            'ZOOM' : '',
            'ZOOMIN' : '',
            'ZOOMOUT' : '',
          
            }
        for i in range(1, 25):
            self._linux2x['F%i' % i] = 'F%i' % i 
        for i in range (10):
            self._linux2x['KP%i' % i] = 'KP_%i' % i
        for c in string.ascii_uppercase:
            self._linux2x[c] = c.lower()

        self._x2linux = {
            'XF86Music' : 'SOUND',
            #'XF86Reload' : '',
            #'XF86Word' : '',
            #'XF86Excel' : '',
            #'XF86Spell' : '',
            'XF86Launch4' : '',
            'osfLeft' : '',
            'osfRight' : '',
            'XF86PowerDown' : '',
            'XF86LogOff' : '',
            'SunAgain' : 'REDO',
            }
        for linuxname, xkeysym in self._linux2x.iteritems():
            self._x2linux.setdefault(xkeysym, linuxname)

    def addMapping(self, linuxname, xkeysym):
        self._linux2x[linuxname] = xkeysym
        self._x2linux[xkeysym] = linuxname

    def addMappings(self, x2linux):
        for xkeysym, linuxname in x2linux.iteritems():
            self.addMapping(linuxname, xkeysym)

    def linux2x(self, linuxname):
        return self._linux2x.get(linuxname, '')


    def x2linux(self, keysym):
        return self._x2linux.get(keysym, '')

    def autoMap(self, linuxKeys, xKeys):

        missed = 0
        
        xkeyslower = {}
        for key in xKeys:
            xkeyslower[key.lower()] = key


        linuxnames = linuxKeys.keys()
        linuxnames.sort()
        for linuxname in linuxnames:
            if len(linuxname)== 1: # letter
                self.linux2x[linuxname] = linuxname.lower()
                continue
            #for prefix in ('BRL_', 'F1', 'F2', 'FN_', 'PROG'):
            #    if linuxname.startswith(prefix):
            #        break
            for name in (linuxname.lower(), linuxname, linuxname.upper(),
                         linuxname.capitalize()):
                for prefix in ('', 'ISO_', 'XF86', 'osd', 'Sun', 'hp', 'XF86Audio'):
                    n = prefix + name
                    if n in xKeys:
                        if linuxname not in self.linux2x or not self.linux2x[linuxname]:
                            print " " * 12 + "'%s' : '%s'," % (linuxname, n)
                        #self.linux2x[linuxname] = n
                        #self.x2linux[name] = linuxname
                        break
                else: # not found
                    continue
                break 
            else:
                if linuxname not in self.linux2x:
                    missed += 1
                    print ' ' * 12 + "'%s' : ''," % linuxname
                    pass
                
        print "MISSED:", missed

# ======================================================================
# === Keyboards ===
# ======================================================================

class Keyboard:

    knownBrands = (
        'Acer', 'Asus', 'BTC', 'Cherry', 'Chicony', 'Compaq', 'Cymotion',
        'Dell', 'Diamond', 'Fujitsu-Siemens', 'Genius', 'Honeywell', 'HP',
        'IBM', 'Labtec', 'Logitech', 'Logi', 'Medion', 'Microsoft',
        'Promedion', 'Samsung', 'Sony', 'Toshiba', )   

    def __init__(self, name, brand='', model=''):
        self.valid = True
        self.name = name
        self.brand = brand
        self.model = model
        self.keys = []
        self._keysfixed = False
        
        self.linuxSpares = [
            'FN_F1', 'FN_F2', 'FN_F3', 'FN_F4', 'FN_F5', 'FN_F6',
            'FN_F7', 'FN_F8', 'FN_F9', 'FN_F10', 'FN_F11', 'FN_F12',
            'FN_1', 'FN_2', 'FN_D', 'FN_E', 'FN_F', 'FN_S', 'FN_B']
        self.linuxSpares.reverse() # reverse order due to .pop()
        self.xSpares = [
            'F25', 'F26', 'F27', 'F28', 'F29', 'F30',
            'F31', 'F32', 'F33', 'F34', 'F35',
            'Launch0', 'Launch1', 'Launch2', 'Launch3', 'Launch4',
            'Launch5', 'Launch6', 'Launch7', 'Launch8', 'Launch9',
            'LaunchA', 'LaunchB', 'LaunchC', 'LaunchD', 'LaunchE', 'LaunchF',
            ]
        self.xSpares.reverse()

    def _splitName(self, name):
        lname = name.lower()
        for brand in self.knownBrands:
            if lname.startswith(brand.lower()):
                model = name[len(brand):]
                if model and model[0] in '-_ ':
                    model = model[1:]
                return brand, model
        return '', ''
        
    def _checkKeys(self):
        """ to be invoked by sub classes after all keys are added"""
        self.keys.sort()
        last_scancode = None
        keys = []
        for (scancode, linuxname, xkeysym) in self.keys:
            if scancode == last_scancode:
                # scan codes must be unique
                continue
            keys.append( (scancode, linuxname, xkeysym) )
        self.keys = keys

    def addKey(self, scancode, linuxname=None, xkeysym=None):
        try:
            scancode = int(scancode)
        except ValueError:
            print "Can't convert scancode to int:", scancode
            return
        if not linuxname and not xkeysym:
            if False and scancode in linuxscancodes: # bad idea
                linuxname = linuxscancodes[scancode]
                print "LLL", linuxname
            else:
                pass
                #print "SSS", scancode
            
        if not xkeysym and linuxname:
            xkeysym = linux2x.linux2x(linuxname)
        elif not linuxname and xkeysym:
            linuxname = linux2x.x2linux(xkeysym)
        #    return
        self.keys.append( (scancode, linuxname, xkeysym) )
        self._keysfixed = False

    def fixKeys(self, removeempty=True):
        self.keys.sort()
        for (scancode, linuxname, xkeysym) in self.keys:
            if linuxname in self.linuxSpares:
                self.linuxSpares.remove(linuxname)
            if xkeysym in self.xSpares:
                self.xSpares.remove(xkeysym)
        keys = []
        for scancode, linuxname, xkeysym in self.keys:
            if not linuxname and not xkeysym and removeempty:
                continue
            if not linuxname:
                print "Adding linux spare! xkeysym is", xkeysym
                if self.linuxSpares:
                    linuxname = self.linuxSpares.pop()
                else:
                    print "Out of spare linux keys:", linuxname
            #if not xkeysym:
            #    print "Adding X11 spare! keycode is", linuxname
            #    if self.xSpares:
            #        xkeysym = self.xSpares.pop()
            #    else:
            #        print "Out of spare X keyssyms:", xkeysym
            keys.append( (scancode, linuxname, xkeysym) )
        self.keys = keys
        self._keysfixed = True

    def getName(self):
        if self.brand and self.model:
            return "%s-%s" % (self.brand, self.model)
        elif self.brand:
            return self.brand
        else:
            return self.name
            
    def getQuotedName(self):
        name = self.getName()
        name = name.replace(" ", "_")
        name = name.replace("/", "_")
        return name

    def keymap(self, output=sys.stdout, comments=False):
        if not self._keysfixed:
            self.fixKeys()

        for scancode, linuxname, xkeysym in self.keys:
            if not linuxname:
                continue
            if linuxname in linuxkeys:
                keycode = linuxkeys[linuxname]
            elif isinstance(linuxname, int):
                keycode = linuxname
            else:
                output.write("# XXX %s\n" % linuxname)
                continue
            if scancode < 128:
                output.write('setkeycode   %02x %s' % (scancode, keycode))
            else:
                output.write('setkeycode e0%02x %s' % (scancode-128, keycode))
            if comments:
                output.write(' # %s\n' % linuxname)
            else:
                output.write('\n')
                          
    def xmodmap(self, output=sys.stdout):
        if not self._keysfixed:
            self.fixKeys()

        output.write('// %s %s\n' % (self.brand, self.model))
        output.write('partial alphanumeric_keys\n')
        output.write('xkb_symbols "%s" {\n' % self.name)
            
        for scancode, linuxname, xkeysym in self.keys:
            if not xkeysym:
                print 'No xkeysym for keycode', linuxname
                continue
            keycode = xkeycodes.symbol(scancode)
            if not keycode:
                print "No keycode found! Scancode:", repr(scancode), "%X" % scancode, "%02X" % scancode, keycode
            output.write("    key %s { [ %s ] };\n" % (keycode, xkeysym))

        output.write('};\n\n')

    def diff(self, other):
        idx1 = idx2 = 0
        len1 = len(self.keys)
        len2 = len(other.keys)
        diff1 = 0
        diff2 = 0
        while idx1 < len1 and idx2 < len2:                
            scancode1 = self.keys[idx1][0]
            scancode2 = other.keys[idx2][0]
            if scancode1 == scancode2:
                if self.keys[idx1][1] and other.keys[idx2][1] \
                       and self.keys[idx1][1] != other.keys[idx2][1]:
                    diff1 += 1
                    diff2 += 1
                elif self.keys[idx1][2] and other.keys[idx2][2] \
                         and self.keys[idx1][2] != other.keys[idx2][2]:
                    diff1 += 1
                    diff2 += 1
                idx1 += 1
                idx2 += 1
            elif scancode1 < scancode2:
                diff1 += 1
                idx1 += 1
            else: # scancode1 > scancode2
                diff2 += 1
                idx2 += 1
        diff1 += (len1 - idx1)
        diff2 += (len2 - idx2)
        return diff1, diff2

class Keyboards:

    def __init__(self):
        self.keyboards = {}
        self.brands = {}
        self.models = {}

    def addKeyboard(self, keyboard):
        #if keyboard.name in self.keyboards:
        #    raise ValueError, "Keyboard with name %s already exists" % keyboard.name
        self.keyboards[keyboard.name] = keyboard # XXX
        self.brands.setdefault(keyboard.brand, []).append(keyboard)
        self.models.setdefault(keyboard.model, []).append(keyboard)

    def addKeyboard(self, keyboards):
        for keyboard in keyboards:
            self.addKeyboard(keyboard)

    
        

linuxkeys = LinuxKeyCodes('/home/str/ffesti/hotkeys/tools/input.h')
linuxkeycodes = ReverseDict(linuxkeys)
xkeys = XKeysyms()
xkeycodes = XKeycodes()
linux2x = Linux2X()

linux2x.addMappings(xkeys.xkeysyms.extensions)

def main():
    #pprint(xkeycodes._groups_sym2code)
    #pprint(xkeycodes._groups_code2sym)
    #return
    #pprint(xkeys)
    #linux2x.autoMap(linuxkeys, xkeys)
    #pprint(linux2x.linux2x)
    #print len(linux2x.linux2x)

    unused = {}
    for nr in range(128) + range(256, 256+128):
        unused[nr] = None

    for nr, code in enumerate(LinuxKey2Scan):
        scancode = code
        if code > 255:
            scancode = code & 0xFF | 0x80
            
        if unused.has_key(code):
            del unused[code]
        else:
            print "DOUBLE", scancode, nr
        
        print nr, linuxkeycodes.get(nr), scancode, scancode-LinuxKey2X[nr]
    print len(LinuxKey2Scan)
    for key in unused:
        scancode = key
        if key > 255:
            scancode = key & 0xFF | 0x80
                        
        print "%3i %x" % (key, scancode)
    print len(unused)
if __name__=='__main__':
    main()
