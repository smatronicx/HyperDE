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
from ...common import helperlib

class WaveCanvasLegend(object):
    # Mixin class for legend
    legend_imagelist = None
    legend_imageidx = dict()

    def AddToLegend(self, name, colour, element):
        # Add name to legend panel
        if self.legend_imagelist is None:
            # Initialize imagelist
            self.legend_imagelist = wx.ImageList(12, 2)
            self.signal_list.SetImageList(self.legend_imagelist, wx.IMAGE_LIST_SMALL)

        if colour not in self.legend_imageidx:
            # Create bitmap
            bmp = wx.Bitmap(12, 2)
            dc = wx.MemoryDC()
            dc.SelectObject(bmp)
            dc.SetBackground(wx.Brush(wx.Colour(colour), style=wx.SOLID))
            dc.SetBackgroundMode(wx.SOLID)
            dc.Clear()
            dc.SelectObject(wx.NullBitmap)

            idx = self.legend_imagelist.Add(bmp)
            self.legend_imageidx[colour] = idx

        idx = self.signal_list.GetItemCount()
        sig_item = self.signal_list.InsertItem(idx, name, self.legend_imageidx[colour])
        self.signal_list_map[sig_item] = element
