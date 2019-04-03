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
from ...common import helperlib
from .wavecanvasaxis import WaveCanvasAxis as axismixin

class WaveCanvasMouse(object):
    # Mixin class for mouse events
    def OnWMouseLeftDown(self, event):
        # Left click on wcanvas
        x, y = event.GetPosition()
        self.zoom_rect[0] = [x, y]
        self.canvases["wcanvas"].CaptureMouse()

        event.Skip()

    def OnWMouseLeftUp(self, event):
        # Remove zoom box
        self.RemoveZoomBox()
        x, y = event.GetPosition()

        if self.zoom_plot is True:
            # Zoom plot
            self.zoom_plot = False
            print self.zoom_rect
            xrange = [self.zoom_rect[0][0], self.zoom_rect[1][0]]
            yrange = [self.zoom_rect[0][1], self.zoom_rect[1][1]]
            self.ZoomCanvas(xrange=xrange, yrange=yrange)

        else:
            # Select elements
            for id in self.id_select_elements:
                # Unselect all
                self.elements[id].OnUnselect()

            del self.id_select_elements[:]
            for id in self.elements:
                # Plot elements
                ishit = self.elements[id].HitTest(x, y, self.hit_radius)
                if ishit is True:
                    self.elements[id].OnSelect()
                    self.id_select_elements.append(id)

        if self.canvases["wcanvas"].HasCapture() is True:
            self.canvases["wcanvas"].ReleaseMouse()

        self.DrawOnDC("wcanvas")

    def OnWMouseMotion(self, event):
        # Movement on wcanvas
        leftdown = event.LeftIsDown()
        x, y = event.GetPosition()

        if self.zoom_plot is False:
            # Enable zoom with atleast 3x3 box
            dx = abs(x-self.zoom_rect[0][0])
            dy = abs(y-self.zoom_rect[0][1])

            drawbox =  dx > 3 and dy > 3 and leftdown
            if drawbox is True:
                self.zoom_plot = True
                self.zoom_rect[1] = [x, y]
                self.DrawZoomBox()

        else:
            # Draw box for zoom
            self.zoom_rect[1] = [x, y]
            self.DrawZoomBox()

    def DrawZoomBox(self):
        # Draw zoombox on canvas
        pdc = self.pdcs["wcanvas"]
        pdc.RemoveId(self.zoom_rect_id)
        pdc.SetId(self.zoom_rect_id)
        pdc.SetPen(self.pen["axes"])
        pdc.SetBrush(self.brush["zoom"])
        x0 = min(self.zoom_rect[0][0], self.zoom_rect[1][0])
        y0 = min(self.zoom_rect[0][1], self.zoom_rect[1][1])
        w = abs(self.zoom_rect[0][0]-self.zoom_rect[1][0])
        h = abs(self.zoom_rect[0][1]-self.zoom_rect[1][1])
        pdc.DrawRectangle(x0, y0, w, h)
        self.DrawOnDC("wcanvas")

    def RemoveZoomBox(self):
        # Remove zoombox from canvas
        pdc = self.pdcs["wcanvas"]
        pdc.RemoveId(self.zoom_rect_id)
        self.DrawOnDC("wcanvas")

    def ZoomCanvas(self, xrange = None, yrange = None):
        # Zoom plots for given range
        axis_range_old = copy.deepcopy(self.axis_range)
        if xrange is not None:
            # Zoom xaxis
            if xrange[0] != xrange[1]:
                xmin = min(xrange[0], xrange[1])
                xmax = max(xrange[0], xrange[1])

                x0, yx0, yx20 = self.GetCanvasCoordinate([xmin, 0])
                x1, yx1, yx21 = self.GetCanvasCoordinate([xmax, 0])

                if x0 == x1:
                    print "No zoom"
                    return

        if yrange is not None:
            # Zoom yaxis/y2axis
            if yrange[0] != yrange[1]:
                ymin = min(yrange[0], yrange[1])
                ymax = max(yrange[0], yrange[1])

                xx0, y0, y20 = self.GetCanvasCoordinate([0, ymax])
                xx1, y1, y21 = self.GetCanvasCoordinate([0, ymin])

                if y0 == y1 or y20 == y21:
                    print "No zoom"
                    return

        if xrange is not None:
            # Set new range
            self.axis_range["xaxis"] = [x0, x1]

        if yrange is not None:
            # Set new range
            self.axis_range["yaxis"] = [y0, y1]
            self.axis_range["y2axis"] = [y20, y21]

        self.OnSize(None)

    def FitCanvas(self):
        # Fit plots
        self.axis_range = copy.deepcopy(self.axis_limits)
        self.OnSize(None)

    def fitzoom( self, event ):
        self.FitCanvas()
