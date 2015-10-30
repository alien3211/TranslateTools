#!/usr/bin/env python

import getopt

from keylogger import *

import translate

from window import *

list_keys = ['', 'left_shift', 'right_shift', 'left_ctrl', 'right_ctrl', 'left_alt', 'right_alt']

glkey  = 'left_alt'
glchar = 'q'


def usage(res):
    out = ("""Usage:
  ./translateTool.py <OPTS>
  -h         | --help           this help
  -f <from>  | --from <from>    original language
  -t <to>    | --to <to>        destination language
  -l         | --list           list language
  -k <key>   | --key <key>      list language

  Example: 
  ./translateTool.py -f en -t pl

  Example change key:
  [key+char] default 'left_alt+q'
  ./translateTool.py -f en -t pl -k 'left_alt+q'

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


def parseArgs():
    global flang, tlang

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:t:lk:", ["help", "from=", "to=", "list","key="])
    except getopt.GetoptError, err:
        usage(2)

    flang = "auto"
    tlang = "pl"

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

def start_window(t, modifiers, keys):
    if (modifiers[glkey] == True) and (keys == glchar):
        win = Window()
        trans = gtk.clipboard_get().wait_for_text().replace('\n', ' ')
        trans, l_trans = translate.Translate(trans, tlang, flang)
        win.set_data(trans, l_trans)
        win.main()

if __name__ == '__main__':
    parseArgs()

    now = time()
    done = lambda: time() > now + 60

    log(done, start_window)
