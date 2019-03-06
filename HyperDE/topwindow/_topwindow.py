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
from . import topwindowgui as gui

from functools import partial

from ..theme import theme_inst as thm
from .. import console
from .. import netlists
from .. import waveview

# This class is used to set main framework for HyperDE

class TopWindow(gui.TopFrame):
    # This class implements main framework

    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if TopWindow.__instance is None:
            raise ValueError("TopWindow is not initialized")
        return TopWindow.__instance

    def __init__(self, parent=None, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(700, 500), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL):
        # Initialize
        if TopWindow.__instance is not None:
            raise ValueError("The class ""TopWindow"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            TopWindow.__instance = self
            #Create widgets
            super(TopWindow, self).__init__(parent, id, pos, size, style, name)

            # Add widgets
            self._AddWidgets(parent=parent)

    def _AddWidgets(self, parent=None):
        # Add widgets to top window

        # Add console
        bsizer_console = wx.BoxSizer(wx.VERTICAL)
        self.console_panel = console.Console(self.panel_console_wrap, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bsizer_console.Add(self.console_panel, 1, wx.EXPAND |wx.ALL, 0)
        self.panel_console_wrap.SetSizer(bsizer_console)
        self.panel_console_wrap.Layout()
        bsizer_console.Fit(self.panel_console_wrap)

        # Add design builder
        bsizer_desbuild = wx.BoxSizer(wx.VERTICAL)
        self.desbuild_panel = netlists.DesignBuilder(self.panel_desbuild_wrap, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bsizer_desbuild.Add(self.desbuild_panel, 1, wx.EXPAND |wx.ALL, 0)
        self.panel_desbuild_wrap.SetSizer(bsizer_desbuild)
        self.panel_desbuild_wrap.Layout()
        bsizer_desbuild.Fit(self.panel_desbuild_wrap)
        self.desbuild_sash = dict()

        # Add wave viewer
        bsizer_waveview = wx.BoxSizer(wx.VERTICAL)
        self.waveview_panel = waveview.WaveView(self.panel_waveview_wrap, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bsizer_waveview.Add(self.waveview_panel, 1, wx.EXPAND |wx.ALL, 0)
        self.panel_waveview_wrap.SetSizer(bsizer_waveview)
        self.panel_waveview_wrap.Layout()
        bsizer_waveview.Fit(self.panel_waveview_wrap)

    def ShowDesignBuilder(self, show=True, size=16):
        # Show/Hide design builder
        if show is False:
            self.desbuild_sash["pos"] = self.design_splitter.GetSashPosition()
            self.desbuild_sash["pane"] = self.design_splitter.GetMinimumPaneSize()
            self.design_splitter.SetSashInvisible(True)
            self.design_splitter.SetMinimumPaneSize(size)
            self.design_splitter.SetSashPosition(size)
        else:
            self.design_splitter.SetSashInvisible(False)
            self.design_splitter.SetMinimumPaneSize(self.desbuild_sash["pane"])
            self.design_splitter.SetSashPosition(self.desbuild_sash["pos"])
