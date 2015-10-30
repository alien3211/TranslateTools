#!/usr/bin/env python

import getopt

from keylogger import *
import gobject

import translate

from window import *

def usage(res):
    out = ("""Usage:
  ./window.py <OPTS>
  -h         | --help           this help
  -f <from>  | --from <from>    original language
  -t <to>    | --to <to>        destination language
  -l         | --list           list language

  Example: 
  ./window.py -f en -t pl
  """)
    print out
    sys.exit(res)

def list_language():
    with open('list_language.txt','r') as f:
        for line in f:
            l = line.split(' ')
            print "{:<9}{}".format(l[0], (' '.join(l[1:])).replace('\n', ''))


def parseArgs():
    global flang, tlang

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:t:l", ["help", "from=", "to=", "list"])
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

def start_window(t, modifiers, keys):
    if (modifiers["left alt"] == True) and (keys == 'q'):
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
