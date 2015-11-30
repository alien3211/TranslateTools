#!/usr/bin/env python
#-*- coding: utf-8 -*-

import getopt

from keycatch import *

import translate

from window import *

list_keys = ['', 'left_shift', 'right_shift', 'left_ctrl', 'right_ctrl', 'left_alt', 'right_alt']

glkey  = 'left_alt'
glchar = 'q'
flang  = "auto"
tlang  = "pl"
clang  = 5
glxx   = 1
glyy   = 1



def usage(res):
    out = ("""Usage:
  ./translateTool.py <OPTS>
  -h         | --help           this help
  -f <from>  | --from <from>    original language
  -t <to>    | --to <to>        destination language
  -l         | --list           list language
  -k <key>   | --key <key>      keyboard shortcut
  -c <time>  | --count <time>   long the active window (s)
  -m <multi> | --move <multi>   position in window

  Example:
  ./translateTool.py -f en -t pl

  Example change key:
  [key+char] default 'left_alt+q'
  ./translateTool.py -f en -t pl -k 'left_alt+q'

  Example position:
  'x:y' default rigth button window '1:1'
  left top window     '0:0'
  right top window    '1:0'
  left button window  '0:1'
  rigth button window '1:1'

  2 window:
  	firts window
  left top window     '0:0'
  right top window    '0.5:0'
  left button window  '0:1'
  rigth button window '0.5:1'

  	secend window
  left top window     '0:0'
  right top window    '1:0'
  left button window  '0:1'
  rigth button window '1:1'

  ./translateTool.py -m 1:1

  All key: """)
    print out
    print '\n  '.join(list_keys)
    sys.exit(res)

def list_language():
    with open('list_language.txt','r') as f:
        for line in f:
            l = line.split(' ')
            print "{:<9}{}".format(l[0], (' '.join(l[1:])).replace('\n', ''))

def parseKey(arg):
    global glkey, glchar
    arg = arg.split('+')
    if len(arg) == 2:
        if arg[0] in list_keys:
            glkey, glchar = arg
        else:
            usage(2)
    else:
        usage(2)

def parseMove(arg):
    global glxx, glyy
    glxx, glyy = arg.split(':')

def parseArgs():
    global flang, tlang, clang

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:t:lk:m:c:", ["help", "from=", "to=", "list", "key=", "move=", "count="])
    except getopt.GetoptError, err:
        usage(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage(0)
            sys.exit()
        elif opt in ("-f", "--from"):
            flang = arg
        elif opt in ("-t", "--to"):
            tlang = arg
        elif opt in ("-l", "--list"):
            list_language()
            sys.exit(0)
        elif opt in ("-k", "--key"):
            parseKey(arg)
        elif opt in ("-m", "--move"):
            parseMove(arg)
        elif opt in ("-c", "--count"):
	    clang = arg

def start_window(t, modifiers, keys):
    if (modifiers[glkey] == True) and (keys == glchar):
	clipboard_primary = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
	clipboard = gtk.clipboard_get()
        trans = str(clipboard_primary.wait_for_text()).replace('\n', ' ')
	trans = trans[:255]
        trans, l_trans = translate.Translate(trans, tlang, flang)
	clipboard.set_text(list(l_trans)[0])
	clipboard.store()
        win = Window(clang, glxx, glyy, trans, l_trans)
        win.main()



if __name__ == '__main__':
    parseArgs()

    now = time()
    done = lambda: time() > now + 60

    log(done, start_window)
