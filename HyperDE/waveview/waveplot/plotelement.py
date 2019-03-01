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

class PlotLine():
    # Class to plot element on canvas
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

        # Add to canvas
        self.wavecanvas = wavecanvas
        self.id = self.wavecanvas.AddElement(self)
        self.wavecanvas.BindDraw(self.id, self.Draw)
        self.colour = colour
        self.width = width
        self.style = style

    def Draw(self, scale, offset, bbox=None):
        # Draw element
        # Set pen
        colour = self.colour

        if not isinstance(colour, wx.Colour):
            colour = wx.Colour(colour)

        pen = wx.Pen(colour, self.width, self.style)

        # Set PseudoDC
        pdc = self.wavecanvas.GetPseudoDC()
        pdc.RemoveId(self.id)

        if bbox is None:
            # Plot all data
            pdc.SetId(self.id)
            pdc.SetPen(pen)
            # Scale points
            x = scale[0] * self.x + offset[0]
            y = scale[1] * self.y + offset[1]

            pdc.DrawLines(zip(x,y))
