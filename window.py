#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import gobject
gobject.threads_init()

class Window:
    def _delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def _destroy(self, widget,data=None):
        gtk.main_quit()

    def _press_event(self, window, event):
        self.g = 1

    #use keyloger 
    def _key_press_event(self, window, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        self.tLabelTrans.set_text('key %s (%d) was pressed' % (keyname, event.keyval))

    def set_data(self, translate, result):
        self.tLabelSelect.set_text(translate)
        self.window.set_size_request(300,100+(15*(len(result)-1)))
        self.tLabelTrans.set_text('\n'.join(map(str,result)))
        self._set_position()

    def _set_position(self):
            (w, h) = self.window.get_size()
            x = gtk.gdk.screen_width()
            y = gtk.gdk.screen_height()

            #Set position Left-Button
            self.window.move(x-w, y-h)

    def timer_s(self):
        self.g += 1;
        if self.g == 5:
            gobject.source_remove(self.timer)
            self.window.destroy()
        return True

    def __init__(self):
        self.g = 1
        self.Win()

    def Win(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.window.connect('delete_event', self._delete_event)
        self.window.connect('destroy', self._destroy)
        self.window.connect('button-press-event', self._press_event)
        #use keyloger 
        #self.window.connect('key_press_event', self._key_press_event)

        self.window.set_size_request(300,100)
        self.window.set_keep_above(True)
        self.window.set_resizable(False)
        self.window.set_decorated(False)

        #set position
        self._set_position()

        #Label
        fix = gtk.Fixed()
        self.tLabelSelect = gtk.Label("None")
        fix.put(self.tLabelSelect, 10 , 10)
        self.tLabelTrans = gtk.Label("None")
        fix.put(self.tLabelTrans, 50 , 50)

        self.window.add(fix)
        self.window.show_all()

        self.timer = gobject.timeout_add(1000, self.timer_s)

    def main(self):
        gtk.main()


#dzielenie w pionie [x if ((i+1) % 3) != 0 else x + '\n' for i,x in enumerate(c)] 
