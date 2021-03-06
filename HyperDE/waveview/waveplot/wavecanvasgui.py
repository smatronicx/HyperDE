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
import wx.dataview

###########################################################################
## Class TopPanel
###########################################################################

class TopPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.waveplot_splitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.waveplot_splitter.SetSashGravity( 0 )
		self.waveplot_splitter.Bind( wx.EVT_IDLE, self.waveplot_splitterOnIdle )
		self.waveplot_splitter.SetMinimumPaneSize( 10 )

		self.waveplot_splitter.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.waveplot_splitter.SetMinSize( wx.Size( 100,100 ) )

		self.signal_panel = wx.Panel( self.waveplot_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.signal_list = wx.ListCtrl( self.signal_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_NO_HEADER|wx.LC_REPORT )
		bSizer7.Add( self.signal_list, 1, wx.ALL|wx.EXPAND, 0 )

		self.cursor_data = wx.dataview.DataViewListCtrl( self.signal_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_NO_HEADER|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.cursor_data.Hide()

		bSizer7.Add( self.cursor_data, 1, wx.ALL|wx.EXPAND, 0 )


		self.signal_panel.SetSizer( bSizer7 )
		self.signal_panel.Layout()
		bSizer7.Fit( self.signal_panel )
		self.waveplot_panel = wx.Panel( self.waveplot_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.WANTS_CHARS )
		fgSizer1 = wx.FlexGridSizer( 4, 6, 0, 0 )
		fgSizer1.AddGrowableCol( 2 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.ylcanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.ylcanvas, 1, wx.EXPAND |wx.ALL, 0 )

		self.ycanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.ycanvas, 1, wx.EXPAND |wx.ALL, 0 )

		self.wcanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.wcanvas.SetMinSize( wx.Size( 1,1 ) )

		fgSizer1.Add( self.wcanvas, 1, wx.ALL|wx.EXPAND, 0 )

		self.y2canvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.y2canvas, 1, wx.EXPAND|wx.ALL, 0 )

		self.y2lcanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.y2lcanvas, 1, wx.EXPAND |wx.ALL, 0 )

		self.sb_ver = wx.ScrollBar( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,1 ), wx.SB_VERTICAL )
		fgSizer1.Add( self.sb_ver, 1, wx.ALL|wx.EXPAND, 0 )

		self.m_panel30 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 0 )

		self.xycanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.xycanvas, 1, wx.EXPAND |wx.ALL, 0 )

		self.xcanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.xcanvas, 1, wx.ALL|wx.EXPAND, 0 )

		self.xy2canvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.xy2canvas, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel31 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel32 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel32, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel23 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel24 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 0 )

		self.xlcanvas = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.xlcanvas, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel34 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel35 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel35, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel36 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel36, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel37 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel37, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel38 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel38, 1, wx.EXPAND |wx.ALL, 0 )

		self.sb_hor = wx.ScrollBar( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1,-1 ), wx.SB_HORIZONTAL )
		fgSizer1.Add( self.sb_hor, 1, wx.ALL|wx.EXPAND, 0 )

		self.m_panel22 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel39 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel39, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel40 = wx.Panel( self.waveplot_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self.m_panel40, wx.ID_ANY, u"z", wx.DefaultPosition, wx.Size( 18,18 ), 0 )
		bSizer31.Add( self.m_button1, 0, wx.ALL, 0 )


		self.m_panel40.SetSizer( bSizer31 )
		self.m_panel40.Layout()
		bSizer31.Fit( self.m_panel40 )
		fgSizer1.Add( self.m_panel40, 1, wx.EXPAND |wx.ALL, 0 )


		self.waveplot_panel.SetSizer( fgSizer1 )
		self.waveplot_panel.Layout()
		fgSizer1.Fit( self.waveplot_panel )
		self.waveplot_splitter.SplitVertically( self.signal_panel, self.waveplot_panel, 100 )
		bSizer3.Add( self.waveplot_splitter, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.fitzoom )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fitzoom( self, event ):
		event.Skip()

	def waveplot_splitterOnIdle( self, event ):
		self.waveplot_splitter.SetSashPosition( 100 )
		self.waveplot_splitter.Unbind( wx.EVT_IDLE )


