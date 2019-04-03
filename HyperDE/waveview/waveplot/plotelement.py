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

import numpy as np
import wx

from ...cppmodules import wavefunc as _wavefunc

class PlotElement(object):
    # Base class for plot elements
    wavefunc = _wavefunc.WaveFunc()
    def __init__(self, wavecanvas, xlimits, ylimits):
        # Add to canvas
        self.xaxis_type = "Scaler"
        self.yaxis_type = "Scalar"
        self.name = ""
        self.colour = wx.Colour("white")
        self.y2axis = False
        self.wavecanvas = wavecanvas
        self.id = self.wavecanvas.AddElement(self, xlimits, ylimits)
        self.pdc = self.wavecanvas.GetWaveDC()
        self.is_legend = False

    def GetName(self):
        # Get Name
        return self.name

    def AddToLegend(self, name=None):
        # Add name to legend
        if name is not None:
            self.name = name

        self.wavecanvas.AddToLegend(self.name, self.colour, self)

    def OnDraw(self, scale, offset, redraw = False):
        # Overload function to draw something on canvas
        pass

    def OnSelect(self):
        # Overload function to do something on select
        pass

    def OnUnselect(self):
        # Overload function to do something on unselect
        pass

    def OnDelete(self):
        # Overload function to do something on delete
        pass

    def HitTest(self, x, y, r):
        # Overload function to do hit test
        pass


class PlotLine(PlotElement):
    # Class to plot line on canvas
    def __init__(self, wavecanvas, x, y, colour="white", width=1, style=wx.PENSTYLE_SOLID):
        # Set ndarrays
        if type(x) is np.ndarray:
            self.x = x
        else:
            self.x = np.array(x).astype(np.float64)

        if type(y) is np.ndarray:
            self.y = y
        else:
            self.y = np.array(y).astype(np.float64)

        # Check is x and y are 1D and same size
        x_dim = len(np.shape(self.x))
        y_dim = len(np.shape(self.y))
        x_len = np.shape(x)[0]
        y_len = np.shape(y)[0]

        if x_dim != 1:
            raise ValueError("x should be one dimensional array")

        if y_dim != 1:
            raise ValueError("y should be one dimensional array")

        if x_len != y_len:
            raise ValueError("x and y should be same size")

        self.len = x_len
        self.xlimits = [np.min(x), np.max(x)]
        self.ylimits = [np.min(y), np.max(y)]

        # Add to canvas
        super(PlotLine, self).__init__(wavecanvas, self.xlimits, self.ylimits)

        # Style
        if not isinstance(colour, wx.Colour):
            colour = wx.Colour(colour)

        self.colour = colour
        self.width = width
        self.style = style
        self.sel_width = width+2
        self.unsel_width = width

        # Scaled
        self.x_scale = self.x
        self.y_scale = self.y

    def OnDraw(self, scale, offset, redraw=False):
        # Draw element
        # Set pen
        pen = wx.Pen(self.colour, self.width, self.style)

        # Set PseudoDC
        self.pdc.RemoveId(self.id)

        # Plot all data
        self.pdc.SetId(self.id)
        self.pdc.SetPen(pen)

        if redraw is False:
            # Scale points
            self.x_scale = scale[0] * (self.x + offset[0])
            self.y_scale = scale[1] * (self.y + offset[1])

        self.pdc.DrawLines(zip(self.x_scale,self.y_scale))

    def HitTest(self, x, y, r):
        # Hit test with wave
        ishit = self.wavefunc.HitTest(self.x_scale, self.y_scale, x, y, r)
        if ishit == 1:
            return True

        return False

    def OnSelect(self):
        # Increase line width
        self.width = self.sel_width
        self.OnDraw(1, 0, redraw=True)

    def OnUnselect(self):
        # Reset line width
        self.width = self.unsel_width
        self.OnDraw(1, 0, redraw=True)
