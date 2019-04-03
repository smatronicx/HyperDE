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
import wx.aui

###########################################################################
## Class TopPanel
###########################################################################

class TopPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.SetSashGravity( 0.5 )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		self.m_splitter1.SetMinimumPaneSize( 100 )

		self.m_splitter1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel1 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.signal_list = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		bSizer5.Add( self.signal_list, 1, wx.ALL|wx.EXPAND, 0 )


		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.wv_notebook = wx.aui.AuiNotebook( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_BOTTOM|wx.aui.AUI_NB_CLOSE_BUTTON|wx.aui.AUI_NB_SCROLL_BUTTONS|wx.aui.AUI_NB_TAB_MOVE )
		self.wv_notebook.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.wv_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.wave_panel1 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer13.Add( self.wave_panel1, 1, wx.ALL|wx.EXPAND, 0 )

		self.wave_panel2 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.wave_panel2.Hide()

		bSizer13.Add( self.wave_panel2, 1, wx.ALL|wx.EXPAND, 5 )

		self.wave_panel3 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.wave_panel3.Hide()

		bSizer13.Add( self.wave_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer13 )
		self.m_scrolledWindow1.Layout()
		bSizer13.Fit( self.m_scrolledWindow1 )
		self.wv_notebook.AddPage( self.m_scrolledWindow1, u"a page", False, wx.NullBitmap )
		self.m_panel13 = wx.Panel( self.wv_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel13.SetMinSize( wx.Size( 100,100 ) )

		self.wv_notebook.AddPage( self.m_panel13, u"a page", False, wx.NullBitmap )

		bSizer4.Add( self.wv_notebook, 1, wx.EXPAND |wx.ALL, 0 )

		self.pointer_pos = wx.StaticText( self.m_panel2, wx.ID_ANY, u"(0,0)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pointer_pos.Wrap( -1 )

		self.pointer_pos.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.pointer_pos.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer4.Add( self.pointer_pos, 0, wx.ALL|wx.EXPAND, 0 )


		self.m_panel2.SetSizer( bSizer4 )
		self.m_panel2.Layout()
		bSizer4.Fit( self.m_panel2 )
		self.m_splitter1.SplitVertically( self.m_panel1, self.m_panel2, 150 )
		bSizer3.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

	def __del__( self ):
		pass

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 150 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )


