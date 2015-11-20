#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import gobject
gobject.threads_init()

class Window:
    def __delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def __destroy(self, widget,data=None):
        gtk.main_quit()

    def __press_event(self, window, event):
        self.g = 1

    #use keyloger
    def __key_press_event(self, window, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        self.tLabelTrans.set_text('key %s (%d) was pressed' % (keyname, event.keyval))

    def __set_data(self, translate, result):
	countTrans, translate = self.__split_string(translate, 38)
        self.tLabelSelect.set_text(translate)
	_, result = self.__split_string('\n'.join(map(str,result)), 32)
	countRes = list(result).count('\n')

        self.window.set_size_request(300, 100 + 15 * (countTrans + countRes - 1))

        self.tLabelTrans.set_text(result)

        self.__set_position()

	return countTrans

    def __split_string(self, word, l):
        i = 0
        new_word = ""
        count = 0
        for x in word:
            if i == l:
                new_word+=x+('\n' if x == ' ' else '-\n')
    	        i = 0
    	        count+=1
	    else:
                new_word+=x
    	        i+=1
        return count, new_word

    def __set_position(self):
            (w, h) = self.window.get_size()
            x = int(gtk.gdk.screen_width()*self.xx)
            y = int(gtk.gdk.screen_height()*self.yy)

            #Set position Left-Button
            self.window.move(x-w, y-h)

    def timer_s(self):
        self.g += 1;
        if self.g >= self.count:
            gobject.source_remove(self.timer)
            self.window.destroy()
        return True

    def __init__(self, count, xx, yy, trans, l_trans):
        self.g = 1
	self.count = int(count)
	self.xx = float(xx)
	self.yy = float(yy)
        self.Win(trans, l_trans)

    def Win(self, trans, l_trans):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.window.connect('delete_event', self.__delete_event)
        self.window.connect('destroy', self.__destroy)
        self.window.connect('button-press-event', self.__press_event)
        #use keyloger
        #self.window.connect('key_press_event', self.__key_press_event)

        self.window.set_size_request(300,100)
        self.window.set_keep_above(True)
        self.window.set_resizable(False)
        self.window.set_decorated(False)

        #Label
        fix = gtk.Fixed()
        self.tLabelSelect = gtk.Label("None")
        self.tLabelTrans = gtk.Label("None")

	posLabTrans = self.__set_data(trans, l_trans)

        fix.put(self.tLabelSelect, 10 , 10)
        fix.put(self.tLabelTrans, 50 , 50 + (15 * posLabTrans))

        self.window.add(fix)
        self.window.show_all()

        self.timer = gobject.timeout_add(1000, self.timer_s)

    def main(self):
        gtk.main()


