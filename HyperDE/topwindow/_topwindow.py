#
# This file is part of HyperDE.
# Copyright (c) 2018 by Smatronicx.
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
import os
import topwindowgui as gui

from functools import partial

from theme import theme_inst as thm
import console
import netlists
import waveview

# This class is used to set main framework for HyperDE

class TopWindow(gui.TopFrame):
    # This class implements main framework

    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if TopWindow.__instance == None:
            raise ValueError("TopWindow is not initialized")
        return TopWindow.__instance

    def __init__(self, parent=None):
        # Initialize
        if TopWindow.__instance != None:
            raise ValueError("The class ""TopWindow"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            #Virtual private constructor
            TopWindow.__instance = self
            #Create widgets
            super(TopWindow, self).__init__(parent, id, pos, size, style, name)
            self._CreateIconList()

            # Add widgets
            self._AddWidgets(parent=parent)

    def _AddWidgets(self, parent=None):
        # Add widgets to top window

        # Add console
        bsizer_console = wx.BoxSizer( wx.VERTICAL )
        self.console_panel = console.Console( self.panel_console_wrap, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bsizer_console.Add( self.console_panel, 1, wx.EXPAND |wx.ALL, 0 )
        self.panel_console_wrap.SetSizer( bsizer_console )
        self.panel_console_wrap.Layout()
        bsizer_console.Fit( self.panel_console_wrap )

        # Add design builder
        bsizer_desbuild = wx.BoxSizer( wx.VERTICAL )
        self.desbuild_panel = netlists.DesignBuilder( self.panel_desbuild_wrap, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bsizer_desbuild.Add( self.desbuild_panel, 1, wx.EXPAND |wx.ALL, 0 )
        self.panel_desbuild_wrap.SetSizer( bsizer_desbuild )
        self.panel_desbuild_wrap.Layout()
        bsizer_desbuild.Fit( self.panel_desbuild_wrap )
        self.desbuild_sash = dict()

        # Add wave viewer
        bsizer_waveview = wx.BoxSizer( wx.VERTICAL )
        self.waveview_panel = waveview.WaveView( self.panel_waveview_wrap, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bsizer_waveview.Add( self.waveview_panel, 1, wx.EXPAND |wx.ALL, 0 )
        self.panel_waveview_wrap.SetSizer( bsizer_waveview )
        self.panel_waveview_wrap.Layout()
        bsizer_waveview.Fit( self.panel_waveview_wrap )

    def _CreateIconList(self):
        # Create icon list from res path
        script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
        icon_path = os.path.join(script_path, "res", "icons")
        self.icon_list = wx.ImageList(16,16)
        self.icon_idx = dict()

        for icon_file in os.listdir(icon_path):
            icon_name = os.path.splitext(icon_file)[0]
            icon_file_full = os.path.join(icon_path, icon_file)
            icon_bmp = wx.Bitmap(icon_file_full, wx.BITMAP_TYPE_ANY)
            self.icon_idx[icon_name] = self.icon_list.Add(icon_bmp)


    def GetIconBitmap(self, name):
        # Get bitmap from icon list
        if self.icon_idx.has_key(name):
            return self.icon_list.GetBitmap(self.icon_idx[name])

        return None

    def GetIconList(self):
        # Get the list of icons
        return self.icon_list

    def GetIconIndex(self, name):
        # Get icon index from icon list
        if self.icon_idx.has_key(name):
            return self.icon_idx.has_key(name)

        return -1

    def ShowDesignBuilder(self, show=True, size=16):
        # Show/Hide design builder
        if show == False:
            self.desbuild_sash["pos"] = self.design_splitter.GetSashPosition()
            self.desbuild_sash["pane"] = self.design_splitter.GetMinimumPaneSize()
            self.design_splitter.SetSashInvisible(True)
            self.design_splitter.SetMinimumPaneSize(size)
            self.design_splitter.SetSashPosition(size)
        else:
            self.design_splitter.SetSashInvisible(False)
            self.design_splitter.SetMinimumPaneSize(self.desbuild_sash["pane"])
            self.design_splitter.SetSashPosition(self.desbuild_sash["pos"])
