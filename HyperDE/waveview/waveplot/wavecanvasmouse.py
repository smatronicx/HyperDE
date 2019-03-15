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

class WaveCanvasMouse(object):
    # Mixin class for mouse events
    def OnWMouseLeftDown(self, event):
        # Left click on wcanvas
        x, y = event.GetPosition()
        self.zoom_rect[0] = [x, y]
        self.canvases["wcanvas"].CaptureMouse()
        bg = self.waveplot_splitter.GetBackgroundColour()
        #cp = self.GetCanvasCoordinate([x, y])
        #print cp
        pdc = self.pdcs["wcanvas"]
        o = pdc.FindObjects(x, y, 1)
        o1 = pdc.FindObjectsByBBox(x, y)
        print x, y, o, o1
        event.Skip()

    def OnWMouseLeftUp(self, event):
        if self.canvases["wcanvas"].HasCapture() is True:
            self.canvases["wcanvas"].ReleaseMouse()
        self.RemoveZoomBox()

    def OnWMouseMotion(self, event):
        # Movement on wcanvas
        dragging = event.Dragging()
        leftdown = event.LeftIsDown()
        x, y = event.GetPosition()

        drawbox = dragging and leftdown
        if drawbox is True:
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
