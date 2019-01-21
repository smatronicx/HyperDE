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
import topwindowgui as gui

from functools import partial

from theme import theme_inst as thm
import console.console as cs

def donothing(tk):
    pass

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
            super(TopWindow, self).__init__(parent=parent)

            bSizer5 = wx.BoxSizer( wx.VERTICAL )
            
            self.m_panel51 = cs.Console( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
            bSizer5.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )


            self.m_panel1.SetSizer( bSizer5 )
            self.m_panel1.Layout()
            bSizer5.Fit( self.m_panel1 )

    def bClick( self, event ):
        print "Hi from button"

    def test(self):
        print self.m_panel1
