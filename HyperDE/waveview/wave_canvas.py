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
import wx.lib.plot

# This class implements basic canvas for plotting

class _PlotGraphics(wx.lib.plot.PlotGraphics):
    #This class extends the existing plot library
    def __init__(self, objects, title='', xLabel='', yLabel=''):
        # Initialize
        super(_PlotGraphics, self).__init__(objects, title, xLabel, yLabel)

    def AddObject(self, object):
        # Add object
        self.objects.append(object)

class _WaveCanvas(wx.lib.plot.PlotCanvas):
    #This class extends the existing plot library
    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        # Initialize
        super(_WaveCanvas, self).__init__(parent, id, pos, size, style, name)
        self.hor_sb = None
        self.ver_sb = None
        self.sb_xunit = 0
        self.sb_xpos = 0
        self.sb_yunit = 0
        self.sb_ypos = 0
        self.tick_colour = wx.WHITE

    def AssignScrollbars(self, hor_sb, ver_sb):
        self.hor_sb = hor_sb
        self.ver_sb = ver_sb
        self.hor_sb.SetScrollbar(0, 1000, 1000, 1000)
        self.ver_sb.SetScrollbar(0, 1000, 1000, 1000)

    def _adjustScrollbars(self):
        # Code taken from plot.PlotCanvas
        # horizontal scrollbar
        r_current = self._getXCurrentRange()
        r_max = list(self._getXMaxRange())
        sbfullrange = float(self.hor_sb.GetRange())

        r_max[0] = min(r_max[0], r_current[0])
        r_max[1] = max(r_max[1], r_current[1])

        unit = (r_max[1] - r_max[0]) / float(self.hor_sb.GetRange())
        pos = int((r_current[0] - r_max[0]) / unit)

        if pos >= 0:
            pagesize = int((r_current[1] - r_current[0]) / unit)
            self.hor_sb.SetScrollbar(pos, pagesize, sbfullrange, pagesize)
            self.sb_xunit = unit
            self.sb_xpos = pos
        else:
            self.hor_sb.SetScrollbar(0, 1000, 1000, 1000)

        # vertical scrollbar
        r_current = self._getYCurrentRange()
        r_max = list(self._getYMaxRange())
        sbfullrange = float(self.ver_sb.GetRange())

        r_max[0] = min(r_max[0], r_current[0])
        r_max[1] = max(r_max[1], r_current[1])

        unit = (r_max[1] - r_max[0]) / sbfullrange
        pos = int((r_current[0] - r_max[0]) / unit)

        if pos >= 0:
            pagesize = int((r_current[1] - r_current[0]) / unit)
            pos = (sbfullrange - 1 - pos - pagesize)
            self.ver_sb.SetScrollbar(pos, pagesize, sbfullrange, pagesize)
            self.sb_yunit = unit
            self.sb_ypos = pos
        else:
            self.ver_sb.SetScrollbar(0, 1000, 1000, 1000)

    def OnScroll(self, event):
        # Scroll the graph base on scrollbar
        sbpos = event.GetPosition()
        if event.GetOrientation() == wx.VERTICAL:
            dist = -1*self.sb_yunit*(sbpos-self.sb_ypos)
            self.ScrollUp(dist)

        if event.GetOrientation() == wx.HORIZONTAL:
            dist = self.sb_xunit*(sbpos-self.sb_xpos)
            self.ScrollRight(dist)

    def _drawAxesValues(self, dc, p1, p2, scale, shift, xticks, yticks):
        # Code taken from plot.PlotCanvas
        # get the tick lengths so that labels don't overlap
        xTickLength = self.tickLengthPrinterScale[0]
        yTickLength = self.tickLengthPrinterScale[1]
        # only care about negative (out of plot area) tick lengths.
        xTickLength = xTickLength if xTickLength < 0 else 0
        yTickLength = yTickLength if yTickLength < 0 else 0

        dc.SetTextForeground(self.tick_colour)

        axes = self.enableAxesValues
        if self.xSpec != 'none':
            if axes.bottom:
                labels = [tick[1] for tick in xticks]
                coords = []
                for x, label in xticks:
                    w = dc.GetTextExtent(label)[0]
                    pt = wx.lib.plot.utils.scale_and_shift_point(x, p1[1], scale, shift)
                    coords.append(
                        (pt[0] - w/2,
                         pt[1] + 2 * self._pointSize[1] - xTickLength)
                    )
                dc.DrawTextList(labels, coords)

            if axes.top:
                labels = [tick[1] for tick in xticks]
                coords = []
                for x, label in xticks:
                    w, h = dc.GetTextExtent(label)
                    pt = wx.lib.plot.utils.scale_and_shift_point(x, p2[1], scale, shift)
                    coords.append(
                        (pt[0] - w/2,
                         pt[1] - 2 * self._pointSize[1] - h - xTickLength)
                    )
                dc.DrawTextList(labels, coords)

        if self.ySpec != 'none':
            if axes.left:
                h = dc.GetCharHeight()
                labels = [tick[1] for tick in yticks]
                coords = []
                for y, label in yticks:
                    w = dc.GetTextExtent(label)[0]
                    pt = wx.lib.plot.utils.scale_and_shift_point(p1[0], y, scale, shift)
                    coords.append(
                        (pt[0] - w - 3 * self._pointSize[0] + yTickLength,
                         pt[1] - 0.5 * h)
                    )
                dc.DrawTextList(labels, coords)

            if axes.right:
                h = dc.GetCharHeight()
                labels = [tick[1] for tick in yticks]
                coords = []
                for y, label in yticks:
                    w = dc.GetTextExtent(label)[0]
                    pt = wx.lib.plot.utils.scale_and_shift_point(p2[0], y, scale, shift)
                    coords.append(
                        (pt[0] + 3 * self._pointSize[0] + yTickLength,
                         pt[1] - 0.5 * h)
                    )
                dc.DrawTextList(labels, coords)

    #def OnMouseLeftDown(self, event):
    #    pt = self.GetXY(event)
    #    print self.GetClosestPoints(pt)

class AnalogWaveCanvas(wx.Panel):
    # This class implements basic canvas for analog waveform plotting
    def __init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        # Initialize
        super(AnalogWaveCanvas, self).__init__(parent, id, pos, size, style, name)
        # Create widgets
        self._CreateWidgets()

    def _CreateWidgets(self):
        # Create widgets

        #Create the canvas
        fgsizer = wx.FlexGridSizer(2, 2, 0, 0)
        self.wave_canvas = _WaveCanvas(self, wx.ID_ANY, wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL)
        self.hor_sb = wx.ScrollBar(self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.SB_HORIZONTAL)
        self.ver_sb = wx.ScrollBar(self, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.SB_VERTICAL)

        fgsizer.Add(self.wave_canvas, 1, wx.EXPAND |wx.ALL, 0 )
        fgsizer.Add(self.ver_sb, 0, wx.EXPAND |wx.ALL, 0 )
        fgsizer.Add(self.hor_sb, 0, wx.EXPAND |wx.ALL, 0 )
        fgsizer.Add(0, 0, wx.EXPAND |wx.ALL, 0 )

        self.SetSizer(fgsizer)
        fgsizer.AddGrowableRow(0, 1)
        fgsizer.AddGrowableCol(0, 1)
        self.Layout()
        self.Fit()

        # Set canvas properties
        self.wave_canvas.SetBackgroundColour(wx.BLACK)
        self.wave_canvas.axesPen = wx.Pen(wx.WHITE, 1.0, wx.PENSTYLE_SOLID)
        self.wave_canvas.tickPen = wx.Pen(wx.WHITE, 1.0, wx.PENSTYLE_SOLID)
        self.wave_canvas.gridPen = wx.Pen(wx.Colour("grey"), 1.0, wx.PENSTYLE_DOT)
        self.wave_canvas.enableZoom = True
        self.wave_canvas.enableDrag = False
        self.wave_canvas.showScrollbars = False
        self.wave_canvas.enableTicks = (True, True)
        self.wave_canvas.enableAxesValues = (True, True)
        self.wave_canvas.fontSizeAxis = 8
        self.wave_canvas.AssignScrollbars(self.hor_sb, self.ver_sb)

        # scrollbar events
        self.Bind(wx.EVT_SCROLL_THUMBTRACK, self.wave_canvas.OnScroll)
        self.Bind(wx.EVT_SCROLL_PAGEUP, self.wave_canvas.OnScroll)
        self.Bind(wx.EVT_SCROLL_PAGEDOWN, self.wave_canvas.OnScroll)
        self.Bind(wx.EVT_SCROLL_LINEUP, self.wave_canvas.OnScroll)
        self.Bind(wx.EVT_SCROLL_LINEDOWN, self.wave_canvas.OnScroll)

        self.hor_sb.Show(True)
        self.ver_sb.Show(True)

    def Draw(self, dc, x=None, y=None):
        self.wave_canvas.Draw(dc,x,y)
