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

from . import waveviewgui as gui
#import wave_canvas
from . waveplot import wavecanvas as wc

# This class implements the waveform viewer

class WaveView(gui.TopPanel):
    # This class implements the waveform viewer
    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if WaveView.__instance is None:
            raise ValueError("WaveView is not initialized")
        return WaveView.__instance

    def __init__(self, parent=None, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(500, 300), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        # Initialize
        if WaveView.__instance is not None:
            raise ValueError("The class ""WaveView"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            WaveView.__instance = self
            #Create widgets
            super(WaveView, self).__init__(parent, id, pos, size, style, name)

            self.TestFigure3(self.wave_panel1)

    def TestFigure3(self, parent):
        import wx.lib.plot

        bsizer = wx.BoxSizer(wx.VERTICAL)
        #plot_canvas = wave_canvas.AnalogWaveCanvas( parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        plot_canvas = wc.WaveCanvas(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bsizer.Add(plot_canvas, 1, wx.EXPAND |wx.ALL, 0)
        parent.SetSizer(bsizer)
        parent.Layout()
        bsizer.Fit(parent)

        #plot_canvas.SetBackgroundColour(wx.BLACK)
        #plot_canvas.axesPen = wx.Pen(wx.WHITE, 1.0, wx.PENSTYLE_SOLID)
        #plot_canvas.tickPen = wx.Pen(wx.WHITE, 1.0, wx.PENSTYLE_SOLID)
        #plot_canvas.xSpec = 3
        #plot_canvas.ySpec = 3
        #plot_canvas.enableCenterLine = True

        #plot_canvas = wx.lib.plot.PlotCanvas(self.wave_panel1)
        data = [[1, 10], [2, 5], [3, 10], [4, 5], [4.5, 5.5]]
        line = wx.lib.plot.PolyLine(data, colour='green', width=2)
        marker = wx.lib.plot.PolyMarker(data, marker='circle', colour='red', width=1)
        data = [[1, 5], [2,4], [3, 3], [4, 4], [4.5, 5]]
        line2 = wx.lib.plot.PolyLine(data, colour='yellow', width=2)
        data = []

        import time

        start = time.time()

        for a in range(1,10):
            b = a%2
            d = [a,b]
            data.append(d)

        end = time.time()
        print "Time: ", end - start

        start = time.time()
        line3 = wx.lib.plot.PolyLine(data, colour='red', width=2)
        end = time.time()
        print "Time: ", end - start

        from .waveplot import plotelement as pe

        pe.PlotLine(plot_canvas, [1, 2, 10, 20], [1, 2, 3, 400], colour="red", width=2)
        pe.PlotLine(plot_canvas, [1, 2, 3, 10, 20, 30], [1, 4, 9, 100, 400, 900], colour="yellow", width=2)

        #plot_canvas.enableZoom = True
        #plot_canvas.showScrollbars = False
        #plot_canvas.enableTicks = (True, True)

        #gc = wx.lib.plot.PlotGraphics([line, marker], '', 'x', 'y')
        #gc = wave_canvas._PlotGraphics([line])
        #gc.AddObject(marker)
        #gc.AddObject(line2)
        #gc.AddObject(line3)

        #x = (1.0, 4.5)
        #y = (0.0, 10.0)

        #start = time.time()
        #plot_canvas.Draw(gc)
        #end = time.time()
        #print "Time: ", end - start
