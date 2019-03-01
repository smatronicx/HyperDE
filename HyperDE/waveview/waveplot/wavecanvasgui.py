# -*- coding: utf-8 -*-
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperDE. If not, see <https://www.gnu.org/licenses/>.
#

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class TopPanel
###########################################################################

class TopPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter2.SetSashGravity( 1 )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		self.m_splitter2.SetMinimumPaneSize( 10 )

		self.m_splitter2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel7 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel7.SetSizer( bSizer7 )
		self.m_panel7.Layout()
		bSizer7.Fit( self.m_panel7 )
		self.waveplot_panel = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.waveplot_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.waveplot_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		fgSizer1 = wx.FlexGridSizer( 3, 4, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.ycanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 20,-1 ), wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.ycanvas, 1, wx.EXPAND |wx.ALL, 5 )

		self.wcanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.wcanvas, 1, wx.EXPAND |wx.ALL, 0 )

		self.y2canvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 20,-1 ), wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.y2canvas, 1, wx.EXPAND|wx.ALL, 0 )

		self.sb_ver = wx.ScrollBar( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_VERTICAL )
		fgSizer1.Add( self.sb_ver, 1, wx.ALL|wx.EXPAND, 0 )

		self.m_panel17 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 0 )

		self.xcanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.xcanvas, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel20 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel23 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel24 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 0 )

		self.sb_hor = wx.ScrollBar( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_HORIZONTAL )
		fgSizer1.Add( self.sb_hor, 0, wx.ALL|wx.EXPAND, 0 )

		self.m_panel22 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel21 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )


		self.waveplot_panel.SetSizer( fgSizer1 )
		self.waveplot_panel.Layout()
		fgSizer1.Fit( self.waveplot_panel )
		self.m_splitter2.SplitVertically( self.m_panel7, self.waveplot_panel, 100 )
		bSizer3.Add( self.m_splitter2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

	def __del__( self ):
		pass

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 100 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )


