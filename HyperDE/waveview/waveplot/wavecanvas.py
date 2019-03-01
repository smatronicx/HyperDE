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


import wx
import wx.adv
from . import wavecanvasgui as gui

class WaveCanvas(wx.Panel):
    #This class provide wrapped for PseudoDC canvas from drawing
    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(500, 300), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        wx.Panel.__init__ (self, parent, id = id, pos = pos, size = size, style = style, name = name)

        # Create canvas with scrollbars
        sizer = wx.FlexGridSizer(3, 4, 0, 0)
        self.wcanvas = wx.Panel(self, wx.ID_ANY, size=wx.Size(100, 100))
        self.xcanvas = wx.Panel(self, wx.ID_ANY, size=wx.Size(-1, 10))
        self.ycanvas = wx.Panel(self, wx.ID_ANY, size=wx.Size(-1, 10))
        self.y2canvas = wx.Panel(self, wx.ID_ANY, size=wx.Size(-1, 10))
        self.sb_ver = wx.ScrollBar(self, wx.ID_ANY, style=wx.SB_VERTICAL)
        self.sb_ver.SetScrollbar(0, 1000, 1000, 1000)
        self.sb_hor = wx.ScrollBar(self, wx.ID_ANY, style=wx.SB_HORIZONTAL)
        self.sb_hor.SetScrollbar(0, 1000, 1000, 1000)

        sizer.Add(self.ycanvas, 1, wx.RIGHT| wx.ALL, 5)
        sizer.Add(self.wcanvas, 1, wx.EXPAND| wx.ALL, 5)
        sizer.Add(self.y2canvas, 1, wx.LEFT| wx.ALL, 5)
        sizer.Add(self.sb_ver, 0, wx.EXPAND| wx.ALL, 5)
        sizer.Add((0, 0))
        sizer.Add(self.xcanvas, 0, wx.EXPAND| wx.ALL, 5)
        sizer.Add((0, 0))
        sizer.Add((0, 0))
        sizer.Add(self.sb_hor, 0, wx.EXPAND| wx.ALL, 5)
        sizer.Add((0, 0))
        sizer.Add((0, 0))

        self.y2canvas.Show(False)

        self.sb_ver.Show(True)
        self.sb_hor.Show(True)

        self.SetSizer(sizer)
        sizer.AddGrowableRow(0, 1)
        sizer.AddGrowableCol(1, 1)
        self.Fit()

        self.SetBackgroundColour("black")
        self.SetForegroundColour("white")

        # create a PseudoDC to record our drawing
        self.pdc = wx.adv.PseudoDC()

        # Pens
        self.pointsize = 1.0
        self.pen = dict()
        self.pen["grid"] = wx.Pen(wx.Colour("grey"), self.pointsize, wx.PENSTYLE_DOT)
        self.pen["centerline"] = wx.Pen(wx.RED, self.pointsize, wx.PENSTYLE_SHORT_DASH)
        self.pen["axes"] = wx.Pen(wx.WHITE, self.pointsize, wx.PENSTYLE_SOLID)
        self.pen["tick"] = wx.Pen(wx.WHITE, self.pointsize, wx.PENSTYLE_SOLID)
        self.tick_length = 2
        self.axes_font_size = 8

        # Callbacks for elements
        self.elements = dict()
        self.on_draw_cb = dict()
        self.on_remove_cb = dict()
        self.on_select_cb = dict()

        # Window event
        self.wcanvas.Bind(wx.EVT_PAINT, self.OnPaint)
        self.wcanvas.Bind(wx.EVT_SIZE, self.OnSize)

        # Axes
        self.axes_id = wx.NewId()
        self.x_axis_lim = [0, 1]
        self.y_axis_lim = [0, 1]
        self.y2_axis_lim = [0, 1]
        self.plot_lim = None

        self.last_draw = 1
        self.OnSize(None)

    def OnSize(self, event):
        # The Buffer init is done here, to make sure the buffer is always
        # the same size as the Window
        size = self.wcanvas.GetClientSize()
        size.width = max(1, size.width)
        size.height = max(1, size.height)

        # Make new offscreen bitmap: this bitmap will always have the
        # current drawing in it, so it can be used to save the image to
        # a file, or whatever.
        self._buffer = wx.Bitmap(size.width, size.height)
        self.Clear()

    def Clear(self):
        # Clear canvas
        dc = wx.ClientDC(self.wcanvas)
        dc = wx.BufferedDC(dc, self._buffer)
        bg = wx.Brush(self.GetBackgroundColour(), wx.SOLID)
        dc.SetBackground(bg)
        dc.SetBackgroundMode(wx.SOLID)
        dc.Clear()

        dc.SetTextForeground(self.GetForegroundColour())
        dc.SetTextBackground(self.GetBackgroundColour())

        # draw to the dc
        self.DrawBox(dc)
        #print self.pdc.FindObjects(1,1,2)
        #self.pdc.DrawToDCClipped(dc,r)

        size = self.wcanvas.GetClientSize()
        offset = (-1*size.width, size.height) #(10,size.height-10)
        scale_x = 1*2*(size.width-20.0)/20.0
        scale_y = -1*2*(size.height-20.0)/40.0
        scale = [scale_x, scale_y]

        for idx in self.on_draw_cb:
            self.on_draw_cb[idx](scale, offset)

        dc.SetClippingRegion(10,10,size.width-10,size.height-10)
        #self.pdc.DrawToDCClipped(dc, wx.Rect(10,10, 10, 10))
        self.pdc.DrawToDC(dc)
        dc.DestroyClippingRegion()
        #self.pdc.DrawToDC(dc)

    def OnPaint(self, event):
        # On paint, redraw graphics
        dc = wx.BufferedPaintDC(self.wcanvas, self._buffer)

    def DrawBox(self, dc):
        size = self.wcanvas.GetClientSize()
        dc.SetPen(self.pen["axes"])
        dc.DrawLine(10,10,size.width-10,10)
        dc.DrawLine(10,size.height-10,size.width-10,size.height-10)
        dc.DrawLine(10,10,10,size.height-10)
        dc.DrawLine(size.width-10,10,size.width-10,size.height-10)

    def DrawLine(self):
        pen = self.pen["axes"]
        id = wx.NewId()
        self.pdc.SetId(id)
        self.pdc.SetPen(pen)
        self.pdc.DrawLine(0,0,10,10)
        r = wx.Rect(0,0,10,10)
        r.Inflate(pen.GetWidth(),pen.GetWidth())
        self.pdc.SetIdBounds(id,r)
        #print id

    def AddElement(self, element):
        # Return id of new element
        id = wx.NewId()
        self.elements[id] = element
        return id

    def BindDraw(self, id, func):
        # Bind draw callback
        self.on_draw_cb[id] = func

    def GetPseudoDC(self):
        # Return PseudoDC
        return self.pdc

    def Draw(self, bbox=None):
        # Draw items on canvas
        self.DrawAxes(bbox)

    def DrawAxes(self, bbox=None):
        # Draw axes
        pass

    def SetTextSize(self, size):
        # Set size of text for PseudoDC
        f = self.GetFont()
        f = wx.Font(int(size), f.GetFamily(), f.GetStyle(), f.GetWeight())
        self.pdc.SetFont(f)

    def GetTextBBox(self, str):
        # Get the bbox
        pass
