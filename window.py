#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

from keylogger import *

class Window:
    def _delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def _destroy(self, widget,data=None):
        gtk.main_quit()

    def _press_event(self, window, event):
        self.tLabelSelect.set_text('Zmiana')
        self.tLabelTrans.set_text('Zmiana')

    def _key_press_event(self, window, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        self.tLabelTrans.set_text('key %s (%d) was pressed' % (keyname, event.keyval))

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.window.connect('delete_event', self._delete_event)
        self.window.connect('destroy', self._destroy)
        self.window.connect('button-press-event', self._press_event)

        self.window.connect('key_press_event', self._key_press_event)

        self.window.set_size_request(300,100)
        self.window.set_keep_above(True)
        self.window.set_resizable(False)
        self.window.set_decorated(False)
        self.window.set_border_width(10)

        (w, h) = self.window.get_size()
        x = gtk.gdk.screen_width()
        y = gtk.gdk.screen_height()

        #Set position Left-Button
        self.window.move(x-w, y-h)

        #Label
        fix = gtk.Fixed()

        self.tLabelSelect = gtk.Label("None")
        fix.put(self.tLabelSelect, 10 , 10)
        self.tLabelTrans = gtk.Label("None1")
        fix.put(self.tLabelTrans, 150 , 50)

        self.window.add(fix)

        self.window.show_all()

    def main(self):
        gtk.main()


win = Window()
win.main()
