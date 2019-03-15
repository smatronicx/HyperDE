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

class WaveCanvasAxis(object):
    # Mixin class for axis drawing
    def SetAxisPDC(self, pdc):
        # Set the options for axis PDC
        pdc.RemoveAll()
        pdc.SetId(wx.NewId())
        pdc.SetPen(self.pen["axes"])
        fg = self.waveplot_splitter.GetForegroundColour()
        bg = self.waveplot_splitter.GetBackgroundColour()
        pdc.SetTextForeground(fg)
        pdc.SetTextBackground(bg)
        self.SetTextSize(self.axis_font, pdc)

    def DrawXAxis(self):
        # Draw X axis
        if self.axis_show["xaxis"] is True:
            height = self.GetXAxisHeight()
        else:
            y = self.axis_ref_label
            lyw, lyh = self.GetAxisLabelSize(y)
            height = lyh/2

        self.canvases["xcanvas"].SetMinSize(wx.Size(-1,height))
        width, height = self.canvases["xcanvas"].GetClientSize()

        # Clear xcanvas
        pdc = self.pdcs["xcanvas"]
        self.SetAxisPDC(pdc)
        del self.grid_xmajor_points[:]
        del self.grid_xminor_points[:]

        # Get major grid line
        x0 = self.axis_range["xaxis"][0]
        x1 = self.axis_range["xaxis"][1]

        lrw, lrh = self.GetAxisLabelSize(self.axis_ref_label)
        lx0w, lx0h = self.GetAxisLabelSize(x0)
        lx1w, lx1h = self.GetAxisLabelSize(x1)

        xstart = self.grid_margin # margin on either side
        ystart = 1
        xend = width - self.grid_margin
        ngrid = math.floor(1.0*(xend - xstart)/lrw)
        ngrid = min(ngrid, self.grid_max_points)
        ngrid = max(self.grid_min_points, ngrid)
        self.axis_bbox.SetLeft(xstart)
        self.axis_bbox.SetRight(xend)

        self.axis_scale[0] = (xend-xstart)/(1.0*(x1 - x0))
        self.axis_offset[0] = xstart/self.axis_scale[0] - 1.0*x0

        # Get labels
        xlabels = self.GetEasyAxisLabels(x0, x1, ngrid)
        xscale = (xend - xstart)/(1.0*(x1 - x0))
        minor_step = (xlabels[1][0]-xlabels[0][0])/(1.0*self.axis_minor_tick_count)
        minor_step = minor_step * xscale

        pdc.DrawLine(xstart, ystart, xend, ystart)
        for xlabel in xlabels:
            # Draw major axis
            x = xscale*(xlabel[0] - x0) + xstart
            pdc.DrawLine(x ,ystart, x, ystart+self.axis_major_tick_len)
            self.grid_xmajor_points.append(x)

            # Draw minor axis
            for i in range(0, self.axis_minor_tick_count):
                x = x + minor_step
                if x < xend:
                    pdc.DrawLine(x ,ystart, x, ystart+self.axis_minor_tick_len)
                    self.grid_xminor_points.append(x)

        # Draw missin minor axis from start
        x = xscale*(xlabels[0][0] - x0) + xstart
        for i in range(0, self.axis_minor_tick_count):
            x = x - minor_step
            if x > xstart:
                pdc.DrawLine(x ,ystart, x, ystart+self.axis_minor_tick_len)
                self.grid_xminor_points.append(x)

        show_label = self.axis_label_show["xaxis"] and self.axis_show["xaxis"]
        if show_label is True:
            # Show labels
            for xlabel in xlabels:
                x = xscale*(xlabel[0] - x0) + xstart
                s = self.GetTextDisplaySize(xlabel[1], self.axis_font)
                xl = x - s.width/2
                pdc.DrawText(xlabel[1], xl, ystart+self.axis_major_tick_len + 2)

            # Hack to fix clipped labels
            # Left of axis
            pdc = self.pdcs["xycanvas"]

            s = self.GetTextDisplaySize(xlabels[0][1], self.axis_font)
            x = xscale*(xlabels[0][0] - x0) + xstart
            xl = x - s.width/2
            if xl < 0:
                widthxy, heightxy = self.canvases["xycanvas"].GetClientSize()
                x = x - xstart + widthxy + self.grid_margin
                xl = x - s.width/2
                pdc.DrawText(xlabels[0][1], xl, ystart+self.axis_major_tick_len + 2)

            # Right of axis
            pdc = self.pdcs["xy2canvas"]
            self.SetAxisPDC(pdc)

            s = self.GetTextDisplaySize(xlabels[-1][1], self.axis_font)
            x = xscale*(xlabels[-1][0] - x0) + xstart
            xl = x + s.width/2
            if xl > width:
                x = - self.grid_margin
                xl = x - s.width/2
                pdc.DrawText(xlabels[-1][1], xl, ystart+self.axis_major_tick_len + 2)

        show_title = self.axis_title_show["xaxis"] and self.axis_show["xaxis"]
        if show_title is True:
            # x axis title
            pdc = self.pdcs["xlcanvas"]
            self.SetAxisPDC(pdc)
            s = self.GetTextDisplaySize("xtitle", self.axis_font)
            self.canvases["xlcanvas"].SetMinSize(wx.Size(-1, s.height+2))
            widthxl, heightxl = self.canvases["xlcanvas"].GetClientSize()
            x = widthxl/2 - s.width/2
            y = 0
            pdc.DrawText("xtitle", x, y)

    def DrawYAxis(self):
        # Draw Y axes
        if self.axis_show["yaxis"] is True:
            width = self.GetYAxisWidth()
        else:
            x = self.axis_range["xaxis"][0]
            lxw, lxh = self.GetAxisLabelSize(x)
            width = lxw/2

        self.canvases["ycanvas"].SetMinSize(wx.Size(width, -1))
        width, height = self.canvases["ycanvas"].GetClientSize()

        # Clear xcanvas
        pdc = self.pdcs["ycanvas"]
        self.SetAxisPDC(pdc)
        del self.grid_ymajor_points[:]
        del self.grid_yminor_points[:]

        # Get major grid line
        y0 = self.axis_range["yaxis"][0]
        y1 = self.axis_range["yaxis"][1]

        lrw, lrh = self.GetAxisLabelSize(self.axis_ref_label)
        ly0w, ly0h = self.GetAxisLabelSize(y0)
        ly1w, ly1h = self.GetAxisLabelSize(y1)

        xstart = width - 1
        ystart = self.grid_margin + ly1h/2 # margin on either side
        yend = height - self.grid_margin
        ngrid = math.floor(1.0*(yend - ystart)/self.grid_min_pixel)
        ngrid = min(ngrid, self.grid_max_points)
        ngrid = max(self.grid_min_points, ngrid)
        self.axis_bbox.SetTop(ystart)
        self.axis_bbox.SetBottom(yend)

        self.axis_scale[1] = -1.0*(yend-ystart)/(1.0*(y1 - y0))
        self.axis_offset[1] = yend/self.axis_scale[1] - 1.0*y0

        # Get labels
        ylabels = self.GetEasyAxisLabels(y0, y1, ngrid)
        yscale = -1*(yend - ystart)/(1.0*(y1 - y0))
        minor_step = (ylabels[1][0]-ylabels[0][0])/(1.0*self.axis_minor_tick_count)
        minor_step = minor_step * yscale

        pdc.DrawLine(xstart, ystart, xstart, yend)
        self.SetTextSize(self.axis_font, pdc)
        for ylabel in ylabels:
            # Draw major axis
            y = yscale*(ylabel[0] - y0) + yend
            pdc.DrawLine(xstart ,y, xstart - self.axis_major_tick_len, y)
            self.grid_ymajor_points.append(y)

            # Draw minor axis
            for i in range(0, self.axis_minor_tick_count):
                y = y + minor_step
                if y > ystart:
                    pdc.DrawLine(xstart, y, xstart-self.axis_minor_tick_len, y)
                    self.grid_yminor_points.append(y)

        # Draw missing minor axis from start
        y = yscale*(ylabels[0][0] - y0) + yend
        for i in range(0, self.axis_minor_tick_count):
            y = y - minor_step
            if y < yend:
                pdc.DrawLine(xstart, y, xstart-self.axis_minor_tick_len, y)
                self.grid_yminor_points.append(y)

        show_label = self.axis_label_show["yaxis"] and self.axis_show["yaxis"]
        label_width = 0
        if show_label is True:
            # Show labels
            for ylabel in ylabels:
                y = yscale*(ylabel[0] - y0) + yend
                s = self.GetTextDisplaySize(ylabel[1], self.axis_font)
                yl = y - s.height/2
                pdc.DrawText(ylabel[1],xstart - self.axis_major_tick_len - 2 - s.width, yl)
                label_width = max(label_width, s.width)

            # Hack to fix clipped labels
            # Bottom of axis
            pdc = self.pdcs["xycanvas"]

            s = self.GetTextDisplaySize(ylabels[0][1], self.axis_font)
            y = yscale*(ylabels[0][0] - y0) + yend
            yl = y + s.height/2
            if yl > height:
                y = - self.grid_margin
                yl = y - s.height/2
                pdc.DrawText(ylabels[0][1], xstart - self.axis_major_tick_len - 2 - s.width, yl)

        # Fix width
        width = self.GetYAxisWidth(width = label_width)
        self.canvases["ycanvas"].SetMinSize(wx.Size(width, -1))

        show_title = self.axis_title_show["yaxis"] and self.axis_show["yaxis"]
        if show_title is True:
            # y axis title
            pdc = self.pdcs["ylcanvas"]
            self.SetAxisPDC(pdc)
            s = self.GetTextDisplaySize("ytitle", self.axis_font)
            self.canvases["ylcanvas"].SetMinSize(wx.Size(s.height+2,-1))
            widthxl, heightxl = self.canvases["ylcanvas"].GetClientSize()
            x = widthxl/2 - s.height/2
            y = heightxl/2 + s.width/2
            pdc.DrawRotatedText("ytitle", x, y, 90)


    def DrawY2Axis(self):
        # Draw Y2 axes
        if self.axis_show["y2axis"] is True:
            width = self.GetYAxisWidth()
        else:
            x = self.axis_range["xaxis"][1]
            lxw, lxh = self.GetAxisLabelSize(x)
            width = lxw/2

        self.canvases["y2canvas"].SetMinSize(wx.Size(width, -1))
        width, height = self.canvases["y2canvas"].GetClientSize()

        # Clear xcanvas
        pdc = self.pdcs["y2canvas"]
        self.SetAxisPDC(pdc)

        # Get major grid line
        y0 = self.axis_range["y2axis"][0]
        y1 = self.axis_range["y2axis"][1]

        lrw, lrh = self.GetAxisLabelSize(self.axis_ref_label)
        ly0w, ly0h = self.GetAxisLabelSize(y0)
        ly1w, ly1h = self.GetAxisLabelSize(y1)

        xstart = 1
        ystart = self.grid_margin + ly0h/2 # margin on either side
        yend = height - self.grid_margin
        ngrid = math.floor(1.0*(yend - ystart)/self.grid_min_pixel)
        ngrid = min(ngrid, self.grid_max_points)
        ngrid = max(self.grid_min_points, ngrid)

        self.axis_scale[2] = -1.0*(yend-ystart)/(1.0*(y1 - y0))
        self.axis_offset[2] = yend/self.axis_scale[2] - 1.0*y0

        # Get labels
        ylabels = self.GetEasyAxisLabels(y0, y1, ngrid)
        yscale = -1*(yend - ystart)/(1.0*(y1 - y0))
        minor_step = (ylabels[1][0]-ylabels[0][0])/(1.0*self.axis_minor_tick_count)
        minor_step = minor_step * yscale

        pdc.DrawLine(xstart, ystart, xstart, yend)
        self.SetTextSize(self.axis_font, pdc)
        for ylabel in ylabels:
            # Draw major axis
            y = yscale*(ylabel[0] - y0) + yend
            pdc.DrawLine(xstart ,y, xstart + self.axis_major_tick_len, y)

            # Draw minor axis
            for i in range(0, self.axis_minor_tick_count):
                y = y + minor_step
                if y > ystart:
                    pdc.DrawLine(xstart, y, xstart + self.axis_minor_tick_len, y)

        # Draw missin minor axis from start
        y = yscale*(ylabels[0][0] - y0) + yend
        for i in range(0, self.axis_minor_tick_count):
            y = y - minor_step
            if y < yend:
                pdc.DrawLine(xstart, y, xstart + self.axis_minor_tick_len, y)

        show_label = self.axis_label_show["y2axis"] and self.axis_show["y2axis"]
        label_width = 0
        if show_label is True:
            # Show labels
            for ylabel in ylabels:
                y = yscale*(ylabel[0] - y0) + yend
                s = self.GetTextDisplaySize(ylabel[1], self.axis_font)
                yl = y - s.height/2
                pdc.DrawText(ylabel[1],xstart + self.axis_major_tick_len + 2, yl)
                label_width = max(label_width, s.width)

            # Hack to fix clipped labels
            # Bottom of axis
            pdc = self.pdcs["xy2canvas"]

            s = self.GetTextDisplaySize(ylabels[0][1], self.axis_font)
            y = yscale*(ylabels[0][0] - y0) + yend
            yl = y + s.height/2
            if yl > height:
                y = - self.grid_margin
                yl = y - s.height/2
                pdc.DrawText(ylabels[0][1], xstart + self.axis_major_tick_len + 2, yl)

        # Fix width
        width = self.GetYAxisWidth(width = label_width)
        self.canvases["y2canvas"].SetMinSize(wx.Size(width, -1))

        show_title = self.axis_title_show["y2axis"] and self.axis_show["y2axis"]
        if show_title is True:
            # y axis title
            pdc = self.pdcs["y2lcanvas"]
            self.SetAxisPDC(pdc)
            s = self.GetTextDisplaySize("y2title", self.axis_font)
            self.canvases["y2lcanvas"].SetMinSize(wx.Size(s.height+2,-1))
            widthxl, heightxl = self.canvases["y2lcanvas"].GetClientSize()
            x = widthxl/2 - s.height/2
            y = heightxl/2 + s.width/2
            pdc.DrawRotatedText("y2title", x, y, 90)


    def SetTextSize(self, size, dc):
        # Set size of text for PseudoDC
        f = self.GetFont()
        f = wx.Font(int(size), f.GetFamily(), f.GetStyle(), f.GetWeight())
        dc.SetFont(f)

    def GetTextDisplaySize(self, str, size):
        # Get the bbox
        dc = wx.ClientDC(self)
        self.SetTextSize(size, dc)
        return dc.GetTextExtent(str)

    def GetAxisFormatNumber(self, x):
        # Get label is axis format
        if self.axis_engg is True:
            x = helperlib.engg_unit(x)
        else:
            x = helperlib.engg_unit(x, suffix = False)

        return x

    def GetAxisLabelSize(self, x):
        # Get label size for axis
        x = self.GetAxisFormatNumber(x)
        s = self.GetTextDisplaySize(x, self.axis_font)
        return s

    def GetXAxisHeight(self):
        # Get hight for xcanvas
        x0 = self.axis_range["xaxis"][0]
        s = self.GetAxisLabelSize(x0)
        s.height = s.height + self.axis_major_tick_len + 5 # 4 Pixel padding
        return s.height

    def GetYAxisWidth(self, y0=None, width=None):
        # Get height for xcanvas
        if y0 is None:
            y0 = self.axis_ref_label
        s = self.GetAxisLabelSize(y0)
        if width is not None:
            s.width = width
        s.width = s.width + self.axis_major_tick_len + 5 # 4 Pixel padding
        return s.width

    def DrawGrid(self):
        # Draw grid on canvas
        pdc = self.pdcs["wcanvas"]
        pdc.RemoveId(self.grid_id)
        pdc.SetId(self.grid_id)
        fg = self.waveplot_splitter.GetForegroundColour()
        bg = self.waveplot_splitter.GetBackgroundColour()
        pdc.SetTextForeground(fg)
        pdc.SetTextBackground(bg)

        x0 = self.axis_bbox.GetLeft()
        x1 = self.axis_bbox.GetRight()
        y0 = self.axis_bbox.GetTop()
        y1 = self.axis_bbox.GetBottom()

        pdc.SetPen(self.pen["grid_minor"])

        show_minor = self.grid_show and self.grid_show_minor
        if show_minor is True:
            # Draw minor grid
            for x in self.grid_xminor_points:
                pdc.DrawLine(x ,y0, x, y1)

            for y in self.grid_yminor_points:
                pdc.DrawLine(x0 ,y, x1, y)

        pdc.SetPen(self.pen["grid_major"])

        if self.grid_show is True:
            # Draw major grid
            for x in self.grid_xmajor_points:
                pdc.DrawLine(x ,y0, x, y1)

            for y in self.grid_ymajor_points:
                pdc.DrawLine(x0 ,y, x1, y)

    def GetEasyAxisLabels(self, x0, x1, npoint):
        # Get axis labels which are easy to read
        # Get mantissa and exponent
        x0m, x0e = helperlib.frexp10(x0)
        x1m, x1e = helperlib.frexp10(x1)
        x10e = x0e-x1e
        # Normalize
        x0m = x0m*math.pow(10.0, x10e)
        # Get x step
        dx = (x1m-x0m)/(1.0*npoint)
        dxm, dxe = helperlib.frexp10(dx)
        # Get 2 digits after .
        dxm_d2 = (math.floor(100*dxm) - 100*math.floor(dxm))
        # Try to find better step
        dxm = math.floor(dxm)
        if dxm_d2 > 75:
            dxm = dxm + 1.0
        elif dxm_d2 > 50:
            dxm = dxm + 0.75
        elif dxm_d2 > 25:
            dxm = dxm + 0.5
        elif dxm_d2 > 0:
            dxm = dxm + 0.25

        # Convert back to original scale
        dx = dxm*pow(10.0, dxe)*pow(10.0, x1e)
        # List points and labels
        labels = list()
        # Get starting point
        x = x0m / pow(10.0, dxe)
        x = math.ceil(x)*pow(10.0, dxe)*pow(10.0, x1e)
        for i in range(0, int(npoint)):
            labels.append([x, helperlib.engg_unit(x)])
            x = x + dx
            if x > x1:
                break

        if abs((x1 - x)/(1.0*x1)) < 0.001:
            # If last point is within 0.1%, add it
            labels.append([x, helperlib.engg_unit(x)])

        return labels

    def GetCanvasCoordinate(self, point):
        # Get x,y,y2 coordinate from DC point
        cpoint = [0, 0, 0]
        cpoint[0] = point[0]/(1.0*self.axis_scale[0])-self.axis_offset[0]
        cpoint[1] = point[1]/(1.0*self.axis_scale[1])-self.axis_offset[1]
        cpoint[2] = point[1]/(1.0*self.axis_scale[2])-self.axis_offset[2]

        return cpoint

    def GetDCCoordinate(self, cpoint, ony2 = False):
        # Get x,y/y2 coordinate to DC point
        point = [0, 0]
        point[0] = (cpoint[0]+self.axis_offset[0])*self.axis_scale[0]
        if ony2 is False:
            # Get point from y axis
            point[1] = (cpoint[1]+self.axis_offset[1])*self.axis_scale[1]
        else:
            # Get point from y2 axis
            point[1] = (cpoint[1]+self.axis_offset[2])*self.axis_scale[2]

        return point
