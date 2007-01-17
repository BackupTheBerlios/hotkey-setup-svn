#!/usr/bin/python



KeyNameMap = {

    # Audio
    
    "Play" : "XF86AudioPlay",
    "MMPlay" : "XF86AudioPlay",
    
    "Audiostop" : "XF86AudioStop",
    "MMStop" : "XF86AudioStop",
    "MediaStop" : "XF86AudioStop",

    "Play|Pause" : "XF86AudioPause", # XXX
    "AudioPlay|Pause" : "XF86AudioPause",
    "play/pause" : "XF86AudioPause",
    "AudioPlay|AudioPause" : "XF86AudioPause",

    "vol" : "XF86AudioMute", # ???

    "VolumeDown" : "XF86AudioLowerVolume",
    "Volume Down" : "XF86AudioLowerVolume",
    "Volumedown" : "XF86AudioLowerVolume",
    "VoumeDown" : "XF86AudioLowerVolume",
    "Volume-" : "XF86AudioLowerVolume",
    "Leiser" : "XF86AudioLowerVolume",
    "LautstaerkeMinus" : "XF86AudioLowerVolume",

    "VolumeUp" : "XF86AudioRaiseVolume",
    "Volume Up" : "XF86AudioRaiseVolume",
    "Volumeup" : "XF86AudioRaiseVolume",
    "Volume+" : "XF86AudioRaiseVolume",
    "Lauter" : "XF86AudioRaiseVolume",
    "vol-up" : "XF86AudioRaiseVolume",
    "VolmeUp" : "XF86AudioRaiseVolume",
    "LautstaerkePlus" : "XF86AudioRaiseVolume",

    "AudioMut" : "XF86AudioMute",
    "Mute|Unmute" : "XF86AudioMute",
    "Mute" : "XF86AudioMute",
    "mute" : "XF86AudioMute",
    "Ton aus" : "XF86AudioMute",

    # Media

    "Media" : "XF86AudioMedia",
    "MediaPlayer" : "XF86AudioMedia",
    "ModeMediaPlayer" : "XF86AudioMedia",
    "MediaSelect" : "XF86AudioMedia",
    
    "Sound" : "XF86Music",
    "MyMusic" : "XF86Music",
    "My Music" : "XF86Music",
    "MediaMusic" : "XF86Music",
    "OpenMusic" : "XF86Music",

    "AudioBack" : "XF86AudioPrev",

    "Stop|Eject" : "XF86Eject", 
    "MediaEject" : "XF86Eject",
    "Eject1" : "XF86Eject",
    "Eject2" : "XF86Eject",
    "Eject|Close" : "XF86Eject",

    "Rewind" : "XF86AudioRewind", 
    "MMRewind" : "XF86AudioRewind",
    "Rew" : "XF86AudioRewind",

    "Record" : "XF86AudioRecord",

    "CDPlay" : "XF86CD",
    "CdPlayer" : "XF86CD",
    "ModeCD" : "XF86CD",

    # Aplications

    "Abrechen" : "osfCancel",
    "Properties" : "ncdSetup", # XXX
    "Setup" : "ncdSetup", # XXX
    "PowerMan" : "", # ???

    "ContextMenu" : "osfMenu",

    # Files

    "FileManager" : "XF86Explorer",
    "Filemanager" : "XF86Explorer",
    "File" : "XF86Explorer",
    "Files" : "XF86Explorer",
    "OpenFile" : "XF86Explorer",
    
    "NewFile" : "XF86New",
    "New_F" : "XF86New",

    # Navigation

     # check against XF86AudioPrev, XF86AudioNext
    
    "Previous" : "XF86Back",
    "PreTrack" : "XF86Back",
    "MediaBack" : "XF86Back",
    "WebBack" : "XF86Back",
    "OBack" : "XF86Back",
    "Prev" : "XF86Back",

    "MediaForward" : "XF86Forward",
    "NextTrak" : "XF86Forward",
    "WebForward" : "XF86Forward",
    "MMForward" : "XF86Forward",
    "OForward" : "XF86Forward",
    "WebFwd" : "XF86Forward",
    "Fwd" : "XF86Forward",

    "Back|Next" : "XF86BackForward",
    
    "MediaLeft" : "Left", # XXX
    "MediaRight" : "Right",
    "MediaUp" : "Up",
    "MediaDown" : "Down",


    "WebStop" : "XF86Stop",

    "Desktop" : "", # XXX

    "My Computer" : "XF86MyComputer",
    "My Com" : "XF86MyComputer",
    "Computer" : "XF86MyComputer",
    "Rechner" : "XF86MyComputer",
    
    "My Documents" : "XF86Documents",
    "MyDocuments" : "XF86Documents",
    "MyDocs" : "XF86Documents",
    "My Doc" : "XF86Documents",
    "MyDOC" : "XF86Documents",

    
    "MyPictures" : "XF86Pictures",
    "My Pictures" : "XF86Pictures",
    "My Pic" : "XF86Pictures",
    "MediaPictures" : "XF86Pictures",
    "OpenPicture" : "XF86Pictures",

    "People" : "", # XXX

    # Screen

    "Zoom" : "XF86ZoomIn XF86ZoomOut", # XXX implement
    "Zoom In" : "XF86ZoomIn",
    "Zoom Out" : "XF86ZoomOut",

    "Rotate" : "XF86RotateWindows",

    "Screen" : "XF86_Next_VMode",

    "Splitscreen" : "XF86SplitScreen",
    "Fullscreen" : "", # XXX
    
    "Screensaver" : "XF86ScreenSaver",
    "LockScreen" : "XF86ScreenSaver",
    "Lock" : "XF86ScreenSaver",
    "Coffe-Key" : "XF86ScreenSaver",
    "Coffee Break" : "XF86ScreenSaver",

    "BrightnessLower" : "SunVideoLowerBrightness", # good idea?
    "BrightnessHigher" : "SunVideoRaiseBrightness", # good idea?

    "Lightbulb" : "XF86LightBulb",
    "Lamp" : "XF86LightBulb",
    
    # Windows
    
    "CloseWindow" : "XF86Close",
    "CycleWindows" : "",




    
    "Datei" : "", # XXX
    "Folder" : "", # XXX
    "Less" : "", # XXX
    "Magnifier" : "", # XXX
    "More" : "", # XXX
    "WebRefresh" : "XF86Refresh",
    "Toggle" : "", # XX
    "Logoff" : "XF86LogOff",
    "Log off" : "XF86LogOff",
    "Log Off" : "XF86LogOff",
    "Replace" : "XF86Paste", # XXX check
    "FastForward" : "", # XXX


    # Start programs
    "UserDefined1" : "XF86Launch1",
    "UserDefined2" : "XF86Launch2",
    "UserDefined3" : "XF86Launch3",
    "UserDefined4" : "XF86Launch4",
    "Custom1" : "XF86Launch1",
    "Custom2" : "XF86Launch2",
    "Launch" : "XF86Launch1",

    "Preset1" : "XF86Launch1",
    "Preset2" : "XF86Launch2",
    "Preset3" : "XF86Launch3",

    "Calc" : "XF86Calculator",
    "calc" : "XF86Calculator",
    "Taschenrechner" : "XF86Calculator",

    "WordProcessor" : "XF86Word",
    "Wordprocessor" : "XF86Word",

    "Spreadsheet" : "XF86Excel",
    "Spreadsheets" : "XF86Excel",

    "Presentation" : "",
    
    "ScreenShot" : "PrintScreen",

    # Web

    "Home" : "XF86HomePage",
    "MyHome" : "XF86HomePage",
    "My Home" : "XF86HomePage",
    "Homepage" : "XF86HomePage",
    "WebHome" : "XF86HomePage",
    "Web|Home" : "XF86HomePage",
    "Startseite" : "XF86HomePage",
    "startseite" : "XF86HomePage",
    "Starseite" : "XF86HomePage",
    "Zuhause" : "XF86HomePage",
    "Web Home" : "XF86HomePage",
    "Web/Home" : "XF86HomePage",
    "home" : "XF86HomePage",

    "Web" : "XF86WWW",
    "Inet" : "XF86WWW",
    "WWWW" : "XF86WWW",
    "Internet" : "XF86WWW",
    "Browser" : "XF86WWW",
    "Web|Stop" : "XF86WWW",
    
    "WebSearch" : "XF86Search",
    "Suchen" : "XF86Search",

    "Communities" : "XF86Community",

    "Bookmark" : "XF86Favorites",
    "Bookmarks" : "XF86Favorites",
    "Favorite" : "XF86Favorites",
    "MyFavorites" : "XF86Favorites",
    "My Favorites" : "XF86Favorites",
    "Favoriten" : "XF86Favorites",
    "My Sites" : "XF86Favorites",

    "WebReload" : "XF86Reload", 

    "Shopping" : "XF86Shop",
    "InternetShopping" : "XF86Shop",
    

    "Print" : "Print",

    "Webcam" : "XF86WebCam",
    "Webkamera" : "XF86WebCam",

    "IBMWebSupport" : "XF86Support",
    "Toshiba" : "XF86Support",
    "DellKey" : "XF86Support",
    "Logitech" : "XF86Support",
    
    "Info" : "Help",
    "Information" : "Help",

    # Mail

    "Email" : "XF86Mail",
    "E-mail" : "XF86Mail",
    "EMail" : "XF86Mail",
    "E-Mail" : "XF86Mail",
    "F/E-Mail" : "XF86Mail",

    "NewMail" : "XF86Mail",
    
    "MailSend" : "XF86Send",
    "MailReply" : "XF86Reply",
    "Reply_All" : "XF86Reply", # XXX check

    "SMS" : "XF86Messenger",
    "Messenger-SMS" : "XF86Messenger",
    "Messenger_SMS" : "XF86Messenger",
    "InstantMsgr" : "XF86Messenger",
    "InstantMessage" : "XF86Messenger",
    "InstantMessanger" : "XF86Messenger",
    "Chat" : "XF86Messenger",

    # Connections
    "Wireless" : "", # XXX
    "Wirless" : "", # XXX
    "Wirelessup" : "", # XXX
    "Wirelessdown" : "", # XXX
    "Bluetooth" : "", # XXX
    "Bluetooht" : "", # XXX
    "BlueLeft" : "",
    "BlueRight" : "",
    "BlueUp|BlueDown" : "",

    # Power
    "Powersaving" : "", # XXX
    "zzZ" : "XF86Sleep",
    "Suspend" : "XF86Sleep",
    "Moon" : "XF86Sleep",
    "Stand By" : "XF86Sleep", # XXX
    "Wake" : "XF86WakeUp",
    "Wake Up" : "XF86WakeUp",
    "Resume" : "XF86WakeUp",
    "Power" : "XF86PowerDown", # XXX

    "Windowskey" : "", # XXX
    "Esettings" : "", # XXX
    "Pbutton" : "", # ??? Power?
    "Ebutton" : "", # ??? Eject? Exploder?
    "Changevga" : "XF86_Next_VMode", # ??? 
    "Touchdown" : "", # ???
    "Touchup" : "", # ???
    "dollar" : None,

    "Questionmark" : None,
    "Dish" : "",
    "Clock" : "",
    "OkSign" : "",
    "P1" : "",
    "P2" : "",
    "P3" : "",
    "Function3" : "",
    "Function4" : "",
    "FunctionSelect" : "",
    "Document1" : "",
    "Document2" : "",
    "Document3" : "",
    "An" : "",
    "NewFolder" : "",
    "Reconnect" : "",
    "Key" : "",
    "WinStart" : "",
    "Journal" : "",
    "Keyboard" : "",
    "PPP" : "",
    "Fan" : "",
    "HP" : "",
    "Photo" : "",
    "Sports" : "",
    "Connect" : "",
    "Entertainment" : "",
    "Fax" : "",
    "TV" : "",
    "Mp3" : "",
    "Security" : "",
    "TouchpadOn" : "",
    "TouchpadOff" : "",
    "Abruf" : "",
    "PsAus" : "",
    "ErAus" : "",
    "Druck" : "",
    "leerLinks" : "",
    "Loesch" : "",
    "Pause" : "",
    "LoeschFeld" : "",
    "Wdgab" : "",
    "leerRechts" : "",
    "WorldBook" : "",
    "devices" : "",
    "power" : "",
    "prev" : "",
    "Status" : "",
    "WinLeft" : "",
    "WinRight" : "",
    "Recieve" : "",
    "F/Bilder" : "",
    "F/Bildschirm" : "",
    "F/Dateien" : "",
    "F/F2" : "",
    "F/F3" : "",
    "F/Musik" : "",
    "F/Play|F/Pause" : "",
    "F/Stop" : "",
    "F/neues" : "",
    "F/vor" : "",
    "F/zurck" : "",
    "Ton" : "",
    "Social" : "",
    "Arrow" : "",
    "ControlPanel" : "",
    "Network" : "",
    "Hotlinks" : "",
    "Shellpress" : "",
    "PreviousPeer" : "",
    "NextPeer" : "",
    "Monitor" : "",
    "Percent" : "",
    "Remote" : "",
    "Burn" : "",
    "Parenthesis_Left" : "",
    "WebSeload" : "",
    "Control" : "",
    "Dos" : "",
    "AlarmStop" : "",
    "Zurueck" : "",
    "Vorwaerts" : "",
    "Abbrechen" : "",
    "Aktual." : "",
    "Wdg|Pause" : "",
    "Stopp" : "",
    "Vorheriger" : "",
    "Naechster" : "",
    "Medien" : "",
    "Arbeitsplatz" : "",
    "Rechner" : "",
    "Taskpane" : "",
    "SpellCheck" : "",
    "Medien|MPlayer" : "",
    "Runterfahren" : "",
    "Mudo" : "",
    "VolMenos" : "",
    "VolMas" : "",
    "Anterior" : "",
    "Reproducir" : "",
    "Siguiente" : "",
    "Parar" : "",
    "Calculadora" : "",
    "Apagar" : "",
    "Suspender" : "",
    "Despertar" : "",
    "S1" : "",
    "UserDefined5" : "",
    "Retry" : "",
    "Foreground" : "",
    "Cute" : "",
    "RadioNetwork" : "",
    "RadioNetworkRelease" : "",
    "Toshiba" : "",
    "ModeOff" : "",
    "Mixer" : "",
    "Update" : "",    

    "Wheelbutton" : None,
    "WheelLeft" : None,
    "WheelRight" : None,
    "WheelClick" : None,
    "EuroSign" : None,
    "AtKey" : None,
    "ParenLeft" : None,
    "ParenRight" : None,
    "LWindows" : None,
    "RWindows" : None,
    }

for i in range(1, 25):
    KeyNameMap['F%i' % i] = 'F%i' % i
    KeyNameMap['FTaste-F%i' % i] = 'F%i' % i
    KeyNameMap['AltF%i' % i] = '%i' % i
    KeyNameMap['fnF%i' % i] = 'F%i' % i
    KeyNameMap['FnF%i' % i] = 'F%i' % i

import re
from hotkeys import *

class LineakKeyboard(Keyboard):
    pass

top = 0
keyboard = 1
keys = 2

class ParseError(ValueError):
    pass

debug = 0

class LineakParser:

    def __init__(self, filename):
        self.filename = filename
        self.keyboards = []

        self.broken = {}
        
    def mapKeyName(self, name):
        if name in KeyNameMap:
            if KeyNameMap[name] == '':
                if debug: print "\t", name
                self.broken.setdefault(name, 0)
                self.broken[name] += 1
            return KeyNameMap[name]
        else:
            for prefix in ('', 'XF86', 'osf', 'hp', 'ap', 'Sun', ):
                if prefix + name in xkeys:
                    return prefix + name
                if prefix + name.lower() in xkeys:
                    return prefix + name.lower()
                if prefix + name.capitalize() in xkeys:
                    return prefix + name.capitalize()
            #print '    "%s" : "",' % name
            self.broken[name] = 1
            KeyNameMap[name] = ''
            if debug: print "\t", name
            #print KeyNameMap.get(name, None)

    def parse(self):
        state = top
        brand = ''
        model = ''
        for nr, line in enumerate(file(self.filename)):
            # remove comments
            line = line.split('#', 1)[0].strip()
            if not line:
                continue
            
            if state == top:
                if line[0]=='[' and line[-1] == ']':
                    name = line[1:-1]
                    state = keyboard
                else:
                    print "Top Line %s: [Keyboardname] expected: %r" % (nr, line)
            elif state == keyboard:
                if line == '[KEYS]':
                    kb = LineakKeyboard(name, brand, model)
                    state = keys
                elif re.match(r'\[END (.+)\]', line):
                    m = re.match(r'\[END (.+)\]', line)
                    state = top
                    kb._checkKeys()
                    self.keyboards.append(kb)
                    if m.group(1) != name and debug:
                        print "Mismatch", name, m.group(1)
                elif line.lower().startswith("rawcommand["):
                    pass
                    if debug: print "Ignoring line %i: %s" % (nr, line)
                else:
                    m = re.match(r'brandname\s*=\s*(.+)', line)
                    if m:
                        brand = m.group(1)
                        if brand[0] in ('"', "'"):
                            brand = brand[1:]
                        if brand[-1] in ('"', "'"):
                            brand = brand[:-1]
                            if debug: print '\n', brand, 
                    else:
                        m = re.match(r'modelname\s*=\s*(.+)', line)
                        if m:
                            model = m.group(1)                            
                            if model[0] in ('"', "'"):
                                model = model[1:]
                            if model[-1] in ('"', "'"):
                                model = model[:-1]
                                if debug: print model
                        else:
                            print "Keyboard Line %s: malformated line %r" % (nr, line)
                            #raise ParseError, "Line %s: malformated line %r" % (nr, line)
            elif state == keys:
                if line in ('[END KEYS]', '[ENDKEYS]'):
                    state = keyboard
                else:
                    m = re.match(r'(.+?)\s*=\s*(\d+)', line)
                    if m:
                        xkeysym = self.mapKeyName(m.group(1))
                        if not linux2x.x2linux(xkeysym):
                            if debug: print m.group(1), xkeysym
                        if not xkeysym:
                            #print "KKK", m.group(1)
                            continue
                        kb.addKey(m.group(2), xkeysym=xkeysym)
                    else:
                        print "Keys line %i: %r" % (nr, line)
                        #raise ParseError, repr(line)


def getKeyboards(
    file="lineakd/lineakkb.def"):
    parser = LineakParser(file)
    parser.parse()
    return [kb for kb in parser.keyboards if kb.valid]

def main():
    parser = LineakParser("/home/ffesti/hotkeys/lineak/lineakd-0.9/lineakd/lineakkb.def")

    parser.parse()

    print "===================================================================="
    #for nr, kb in enumerate(parser.keyboards):
    #    print nr, kb.brand, kb.model
        #kb.xmodmap()
        #kb.keymap()

    broken = [(nr, name) for name, nr in parser.broken.iteritems()]
    broken.sort()
    nr_broken = 0
    for nr, name in broken:
        print name, nr
        nr_broken += nr
    print "Broken", nr_broken

    ok = 0
    known_names = {}
    for kb in parser.keyboards:
        print kb.brand, kb.model
        broken = 0
        for scancode, linuxname, xkeysym in kb.keys:
            if xkeysym in ('',):
                broken += 1
            else:
                known_names[xkeysym] = None
                
        if not broken:
            ok += 1
        else:
            print "\t", broken, len(kb.keys)
    print "OK: %i/%i" % (ok, len(parser.keyboards))

    known_names = known_names.keys()
    known_names.sort()
    print len(known_names)
    for name in known_names:
        if not linux2x.x2linux(name):
            print name

if __name__ == '__main__':
    main()

