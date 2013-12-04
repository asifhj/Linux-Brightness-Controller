#!/usr/bin/env python
# -*- coding:utf-8 -*-
#RandR-based backlight control application
import wx
import subprocess
from os import system
import time

class LinuxBrightnessController(wx.Frame):

    def debug_true(self):
        return False

    def __init__(self, parent, title):
        super(LinuxBrightnessController, self).__init__(parent, title=title, size=(360, 100))
        
        self.name="LVDS1"

        self.value = 0.00
        self.cmds_xrandr_display = []
        
        for i in xrange(0, 101):
            cmd_xrandr_display = "xrandr --output %s --brightness %s" % (self.name, self.value)
            self.cmds_xrandr_display.append(cmd_xrandr_display)
            self.value += 0.01

        self.about_me_message = '''
        # LinuxBrightnessController v0.1

        This application provides a GUI to
        change brightness of Primary and Secondary
        Display.
        Source available at
        https://github.com/asifhj.'''

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        button_about = wx.Button(panel, label='?', size=(25, 25))
        button_about.Bind(wx.EVT_BUTTON, self.about_dialog)
        self.vbox.Add(button_about, flag=wx.ALIGN_RIGHT)

        #Primary device settings panel

        xrandr_row = wx.BoxSizer(wx.HORIZONTAL)
        xbacklight_row = wx.BoxSizer(wx.HORIZONTAL)
        
        xrandr_string = wx.StaticText(panel, label='   Xrandr Primary     ')
        xrandr_row.Add(xrandr_string, flag=wx.RIGHT | wx.TOP, border=3)
        xrandr_slider = wx.Slider(panel, value=100, minValue=1, maxValue=100, size=(200, -1), style=wx.SL_HORIZONTAL)
        xrandr_row.Add(xrandr_slider, flag=wx.LEFT | wx.RIGHT, border=25)
        xrandr_slider.Bind(wx.EVT_SCROLL, self.xrandr_scroll)

        xbacklight_string = wx.StaticText(panel, label='   Xbacklight Primary')
        xbacklight_row.Add(xbacklight_string, flag=wx.RIGHT | wx.TOP, border=3)
        xbacklight_slider = wx.Slider(panel, value=100, minValue=1, maxValue=100, size=(200, -1), style=wx.SL_HORIZONTAL)
        xbacklight_row.Add(xbacklight_slider, flag=wx.LEFT | wx.RIGHT, border=25)
        xbacklight_slider.Bind(wx.EVT_SCROLL, self.xbacklight_scroll)
    
        self.vbox.Add(xrandr_row)
        self.vbox.Add(xbacklight_row)

        panel.SetSizer(self.vbox)

    def xrandr_scroll(self, event):
        """Controls the brightness of primary xrandr monitor"""
        obj = event.GetEventObject()
        val = obj.GetValue()
        system(self.cmds_xrandr_display[val])

    def xbacklight_scroll(self, event):
        """Controls the brightness of primary xbacklight monitor"""
        obj = event.GetEventObject()
        val = obj.GetValue()
        system("xbacklight ="+str(val)+" -time 0 -steps 1")

    def about_dialog(self, event):
        """Shows the about message of LightBox"""
        wx.MessageBox(self.about_me_message, 'About',  wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    LinuxBrightnessController(None, title='Linux-Brightness Controller')
    app.MainLoop()
