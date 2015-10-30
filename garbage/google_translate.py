#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# 2012-11-28 23:09:25.0 +0100 / sputnick <gilles.quenot *AT* gmail>
# ------------------------------------------------------------------------------
# https://github.com/sputnick-dev/google_translate/blob/master/google_translate.py
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of version 2 of the GNU General Public
#    License published by the Free Software Foundation.
# ------------------------------------------------------------------------------
#                                        ,,_
#                                       o"  )@
#                                        ''''
# ------------------------------------------------------------------------------
# vim:ts=4:sw=4

# -----8<--------------------------------------------------------------------------------
url = "http://translate.google.com/"
charset = "utf8"
# -----8<--------------------------------------------------------------------------------
version = 0.3

import mechanize, cookielib, sys, getopt
from lxml import etree

def usage(res):
    out = ("""Usage:
  ./google_translate.py <OPTS>
  -h         | --help           this help
  -f <from>  | --from <from>    original language
  -t <to>    | --to <to>        destination language
  -w <text>  | --words <text>   text
  -v         | --version        google_translate version
  
  Example: 
  ./google_translate.py -f en -t fr -w "A grey hat"
  See http://translate.google.com/about/intl/en_ALL/ for all supported languages""")
    print out
    sys.exit(res)

def browser():
    br = mechanize.Browser(factory=mechanize.RobustFactory())
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open(url)
    br.select_form(nr=0) # select 1st form
    br.find_control(name="sl").value = [flang]
    br.find_control(name="tl").value = [tlang]
    br.form["text"] = words
    br.submit()
    return etree.HTML(br.response().read())

def parseArgs():
    global flang, tlang, words, alt

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:t:w:va", ["help", "from=", "to=", "words=", "version"])
    except getopt.GetoptError, err:
        usage(2)

    flang = None
    tlang = None
    alt = None

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage(0)
            sys.exit()
        elif opt in ("-f", "--from"):
            flang = arg
        elif opt in ("-t", "--to"):
            tlang = arg
        elif opt in ("-w", "--word"):
            words = arg
        elif opt in ("-v", "--version"):
            print version
            sys.exit(0)
        else:
            assert false, "unhandled option"

def main(argv):
    parseArgs()
    if flang is None:
        usage(2)

    reddit = browser()
    result = reddit.xpath('//span[@id="result_box"]/span')

    for r in result:
        print r.text.encode(charset)


if __name__ == "__main__":
    main(sys.argv[1:])
