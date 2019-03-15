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
import random
import copy
import math
from functools import partial
from . import wavecanvasgui as gui
from ...common import helperlib
from .wavecanvasaxis import WaveCanvasAxis as axismixin
from .wavecanvasmouse import WaveCanvasMouse as mousemixin

class WaveCanvas(axismixin, mousemixin, gui.TopPanel):
    #This class provide wrapped for PseudoDC canvas from drawing
    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(500, 300), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        #Create widgets
        super(WaveCanvas, self).__init__ (parent, id = id, pos = pos, size = size, style = style, name = name)

        # create a PseudoDC to record our drawing
        self.pdcs = dict()
        self.pdcs["wcanvas"] = wx.adv.PseudoDC()
        self.pdcs["xcanvas"] = wx.adv.PseudoDC()
        self.pdcs["ycanvas"] = wx.adv.PseudoDC()
        self.pdcs["xycanvas"] = wx.adv.PseudoDC()
        self.pdcs["y2canvas"] = wx.adv.PseudoDC()
        self.pdcs["xy2canvas"] = wx.adv.PseudoDC()
        self.pdcs["xlcanvas"] = wx.adv.PseudoDC()
        self.pdcs["ylcanvas"] = wx.adv.PseudoDC()
        self.pdcs["y2lcanvas"] = wx.adv.PseudoDC()

        # Pens
        self.pointsize = 1.0
        self.pen = dict()
        self.pen["grid_major"] = wx.Pen(wx.Colour("gray"), self.pointsize, wx.PENSTYLE_SOLID)
        self.pen["grid_minor"] = wx.Pen(wx.Colour("gray"), self.pointsize, wx.PENSTYLE_DOT)

        # Brush
        self.brush = dict()
        self.brush["zoom"] = wx.Brush("white", style=wx.BRUSHSTYLE_TRANSPARENT)

        # Callbacks for elements
        self.elements = dict()

        # Canvases
        self.canvases = dict()
        self.canvases["wcanvas"] = self.wcanvas
        self.canvases["xcanvas"] = self.xcanvas
        self.canvases["ycanvas"] = self.ycanvas
        self.canvases["xycanvas"] = self.xycanvas
        self.canvases["y2canvas"] = self.y2canvas
        self.canvases["xy2canvas"] = self.xy2canvas
        self.canvases["xlcanvas"] = self.xlcanvas
        self.canvases["ylcanvas"] = self.ylcanvas
        self.canvases["y2lcanvas"] = self.y2lcanvas

        self.buffers = dict()

        # Window event
        self.wcanvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="wcanvas"))
        self.xcanvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="xcanvas"))
        self.ycanvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="ycanvas"))
        self.xycanvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="xycanvas"))
        self.y2canvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="y2canvas"))
        self.xy2canvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="xy2canvas"))
        self.xlcanvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="xlcanvas"))
        self.ylcanvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="ylcanvas"))
        self.y2lcanvas.Bind(wx.EVT_PAINT, partial(self.OnPaint, canvas="y2lcanvas"))

        self.wcanvas.Bind(wx.EVT_SIZE, self.OnSize)

        # Mouse events
        self.zoom_rect = [[0, 0], [0, 0]]
        self.zoom_rect_id = wx.NewId()
        self.wcanvas.Bind(wx.EVT_LEFT_DOWN, self.OnWMouseLeftDown)
        self.wcanvas.Bind(wx.EVT_MOTION, self.OnWMouseMotion)
        self.wcanvas.Bind(wx.EVT_LEFT_UP, self.OnWMouseLeftUp)
        #self.wcanvas.Bind(wx.EVT_LEAVE_WINDOW, self.OnWMouseLeftUp)

        # Axes
        self.axis_limits = dict()
        self.axis_limits["xaxis"] = [0, 1]
        self.axis_limits["yaxis"] = [0, 1]
        self.axis_limits["y2axis"] = [0, 1]
        self.axis_range = copy.deepcopy(self.axis_limits)
        self.axis_scale = [1, 1, 1]
        self.axis_offset = [0, 0, 0]

        self.axis_bbox = wx.Rect(0, 0, 1, 1)

        self.axis_show = dict()
        self.axis_show["xaxis"] = True
        self.axis_show["yaxis"] = True
        self.axis_show["y2axis"] = True

        self.axis_label_show = dict()
        self.axis_label_show["xaxis"] = True
        self.axis_label_show["yaxis"] = True
        self.axis_label_show["y2axis"] = True

        self.axis_title_show = dict()
        self.axis_title_show["xaxis"] = True
        self.axis_title_show["yaxis"] = True
        self.axis_title_show["y2axis"] = True

        self.axis_ref_label = 123.123123e-12

        self.axis_font = 10
        self.axis_engg = True

        self.axis_major_tick_len = 5
        self.axis_minor_tick_len = 3
        self.axis_minor_tick_count = 5

        # Grid
        self.grid_min_pixel = 50
        self.grin_max_major = 10
        self.grid_show = True
        self.grid_show_minor = True
        self.grid_margin = 5
        self.grid_max_points = 10
        self.grid_min_points = 2

        self.grid_xmajor_points = list()
        self.grid_ymajor_points = list()
        self.grid_xminor_points = list()
        self.grid_yminor_points = list()

        self.grid_id = wx.NewId()

        # Set colour scheme
        self.SetColourScheme(black_bg = True)

        # Set initial buffers
        self.OnSize(None)

    def SetColourScheme(self, black_bg = True):
        # Set the colour scheme of canvas
        # Black backgroud, black_bg=True
        # White backgroud, black_bg=False
        if black_bg is True:
            bg = wx.Colour("black")
            fg = wx.Colour("white")

        else:
            bg = wx.Colour("white")
            fg = wx.Colour("balck")

        # Set colours
        fgpen = wx.Pen(fg, self.pointsize, wx.PENSTYLE_SOLID)

        self.waveplot_splitter.SetBackgroundColour(bg)
        self.waveplot_splitter.SetForegroundColour(fg)

        self.pen["axes"] = fgpen
        self.pen["tick"] = fgpen

        self.brush["bg"] = wx.Brush(bg, style=wx.SOLID)


    def OnSize(self, event):
        # Draw elements on PseudoDC
        self.Draw()

        # Show elements on real DC
        # The Buffer init is done here, to make sure the buffer is always
        # the same size as the Window
        for cv in self.canvases:
            size = self.canvases[cv].GetClientSize()
            size.width = max(1, size.width)
            size.height = max(1, size.height)

            # Make new offscreen bitmap: this bitmap will always have the
            # current drawing in it, so it can be used to save the image to
            # a file, or whatever.
            self.buffers[cv] = wx.Bitmap(size.width, size.height)

            # Draw on real DC
            self.DrawOnDC(cv)

    def DrawOnDC(self, canvas):
        # Show elements on real DC
        dc = wx.ClientDC(self.canvases[canvas])
        dc = wx.BufferedDC(dc, self.buffers[canvas])
        dc.SetBackground(self.brush["bg"])
        dc.SetBackgroundMode(wx.SOLID)
        dc.Clear()
        self.pdcs[canvas].DrawToDC(dc)

    def OnPaint(self, event, canvas=None):
        # On paint, redraw graphics
        canvas=None
        if canvas is None:
            for cv in self.canvases:
                dc = wx.BufferedPaintDC(self.canvases[cv], self.buffers[cv])

        else:
            dc = wx.BufferedPaintDC(self.canvases[canvas], self.buffers[canvas])

    def AddElement(self, element, xlimits, ylimits):
        # Return id of new element
        id = wx.NewId()
        self.SetNewLimits("xaxis", xlimits)
        self.SetNewLimits("yaxis", ylimits)
        self.elements[id] = element
        return id

    def SetNewLimits(self, axis, limits):
        # Set new limits for axis
        cur_limits = self.axis_limits[axis]
        cur_limits[0] = min(cur_limits[0], limits[0])
        cur_limits[1] = max(cur_limits[1], limits[1])
        self.axis_limits[axis] = cur_limits
        self.axis_range[axis] = cur_limits

    def GetWaveDC(self):
        # Return PseudoDC
        return self.pdcs["wcanvas"]

    def Draw(self):
        # Draw items on canvas
        self.SetAxisPDC(self.pdcs["xycanvas"])
        self.SetAxisPDC(self.pdcs["xy2canvas"])
        self.DrawXAxis()
        self.DrawYAxis()
        self.DrawY2Axis()
        self.DrawGrid()
        self.DrawElements()

    def DrawElements(self):
        # Draw elements on canvas
        for id in self.elements:
            # Plot elements
            self.elements[id].OnDraw(self.axis_scale, self.axis_offset)
            self.pdcs["wcanvas"].SetIdBounds(id, self.axis_bbox)
