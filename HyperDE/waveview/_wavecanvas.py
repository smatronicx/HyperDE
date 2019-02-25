#
# This file is part of HyperDE.
# Copyright (c) 2019 by Smatronicx.
# All Rights Reserved.
#
# HyperDE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperDE.  If not, see <https://www.gnu.org/licenses/>.
#


import sys
import wx
import wx.adv

class WaveCanvas(wx.Panel):
    #This class provide wrapped for PseudoDC canvas from drawing
    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        # Create canvas with scrollbars
        sizer = wx.FlexGridSizer(2, 2, 0, 0)
        self.canvas = wx.Window(self, -1)
        self.sb_ver = wx.ScrollBar(self, -1, style=wx.SB_VERTICAL)
        self.sb_ver.SetScrollbar(0, 1000, 1000, 1000)
        self.sb_hor = wx.ScrollBar(self, -1, style=wx.SB_HORIZONTAL)
        self.sb_hor.SetScrollbar(0, 1000, 1000, 1000)

        sizer.Add(self.canvas, 1, wx.EXPAND| wx.ALL, 0)
        sizer.Add(self.sb_ver, 0, wx.EXPAND| wx.ALL, 0)
        sizer.Add(self.sb_hor, 0, wx.EXPAND| wx.ALL, 0)
        sizer.Add((0, 0))

        self.sb_ver.Show(True)
        self.sb_hor.Show(True)

        self.SetSizer(sizer)
        sizer.AddGrowableRow(0, 1)
        sizer.AddGrowableCol(0, 1)
        self.Fit()

        self.SetBackgroundColour("black")
        self.SetForegroundColour("white")

        # create a PseudoDC to record our drawing
        self.pdc = wx.adv.PseudoDC()

        # Pens
        self._pointSize = (1.0, 1.0)
        self._gridPen = wx.Pen(wx.Colour("grey"), self._pointSize[0], wx.PENSTYLE_DOT)

        self._centerLinePen = wx.Pen(wx.RED, self._pointSize[0], wx.PENSTYLE_SHORT_DASH)

        self._axesPen = wx.Pen(wx.WHITE, self._pointSize[0], wx.PENSTYLE_SOLID)

        self._tickPen = wx.Pen(wx.WHITE, self._pointSize[0], wx.PENSTYLE_SOLID)
        self._tickLength = tuple(-x * 2 for x in self._pointSize)

        self._diagonalPen = wx.Pen(wx.BLUE, self._pointSize[0], wx.PENSTYLE_DOT_DASH)

        # Window event
        self.canvas.Bind(wx.EVT_PAINT, self.OnPaint)
        self.canvas.Bind(wx.EVT_SIZE, self.OnSize)

        self.DrawLine()

        self.last_draw = 1
        self.OnSize(None)

    def OnSize(self, event):
        # The Buffer init is done here, to make sure the buffer is always
        # the same size as the Window
        size = self.canvas.GetClientSize()
        size.width = max(1, size.width)
        size.height = max(1, size.height)

        # Make new offscreen bitmap: this bitmap will always have the
        # current drawing in it, so it can be used to save the image to
        # a file, or whatever.
        self._buffer = wx.Bitmap(size.width, size.height)
        self.Clear()

    def Clear(self):
        # Clear canvas
        dc = wx.ClientDC(self.canvas)
        dc = wx.BufferedDC(dc, self._buffer)
        bg = wx.Brush(self.GetBackgroundColour(), wx.SOLID)
        dc.SetBackground(bg)
        dc.SetBackgroundMode(wx.SOLID)
        dc.Clear()

        dc.SetTextForeground(self.GetForegroundColour())
        dc.SetTextBackground(self.GetBackgroundColour())

        # draw to the dc
        r = wx.Rect(0,0,10,10)
        self.DrawBox(dc)
        self.pdc.DrawToDC(dc)
        #print self.pdc.FindObjects(1,1,2)
        #self.pdc.DrawToDCClipped(dc,r)


    def OnPaint(self, event):
        # On paint, redraw graphics
        dc = wx.BufferedPaintDC(self.canvas, self._buffer)

    def DrawBox(self, dc):
        size = self.canvas.GetClientSize()
        dc.SetPen(self._axesPen)
        dc.DrawLine(10,10,size.width-10,10)
        dc.DrawLine(10,size.height-10,size.width-10,size.height-10)
        dc.DrawLine(10,10,10,size.height-10)
        dc.DrawLine(size.width-10,10,size.width-10,size.height-10)

    def DrawLine(self):
        pen = self._axesPen
        id = wx.NewId()
        self.pdc.SetId(id)
        self.pdc.SetPen(pen)
        self.pdc.DrawLine(0,0,10,10)
        r = wx.Rect(0,0,10,10)
        r.Inflate(pen.GetWidth(),pen.GetWidth())
        self.pdc.SetIdBounds(id,r)
        #print id
