#!/usr/bin/env python
#-*- coding: utf-8 -*-


from GoogleTranslate import translate

import xml.etree.ElementTree as ET

import re, os

def Translate(words, to_language="auto", language="auto"):
    raw_words = re.sub('[ \t\r\n]+', ' ', words)
    words = raw_words.lower()
    trans =  [translate(words, to_language, language)]
    if words.find(' ') == -1:
        if len(re.compile('[a-zA-Z]').findall(words[0])) == 1:
	    file_path = '/'.join(os.path.realpath(__file__).split('/')[:-1])
            xml_tree = ET.parse(file_path + '/XML_dict/' + words[0] + '.xml')
	    for node in xml_tree.findall('entry'):
		for child in node.getiterator():
		    if child.tag == 'spl':
			if child.text == words:
			    prev = child #if no example:
			    for line in node.getiterator():
				if line.tag == 'trans' and prev.tag != 'example' and prev.tag != 'idarex': #if no example:
				    trans.append(line.text.encode('UTF8'))
				prev = line # if no example:
			    return [raw_words, set(trans)]
    return [raw_words, trans]
