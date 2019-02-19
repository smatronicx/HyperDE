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
import wx.propgrid as pg

###########################################################################
## Class TopPanel
###########################################################################

class TopPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.BORDER_NONE|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.top_splitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.top_splitter.SetSashGravity( 0.5 )
		self.top_splitter.Bind( wx.EVT_IDLE, self.top_splitterOnIdle )
		self.top_splitter.SetMinimumPaneSize( 100 )

		self.m_panel2 = wx.Panel( self.top_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.design_builder_book = wx.aui.AuiNotebook( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_TAB_FIXED_WIDTH|wx.aui.AUI_NB_TOP )
		self.design_builder_book.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.design_builder_book.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.design_builder_book.SetMinSize( wx.Size( 100,100 ) )

		self.m_panel5 = wx.Panel( self.design_builder_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter2 = wx.SplitterWindow( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter2.SetSashGravity( 0.5 )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		self.m_splitter2.SetMinimumPaneSize( 50 )

		self.m_panel7 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.design_tree = wx.TreeCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_SINGLE )
		self.design_tree.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.design_tree.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer6.Add( self.design_tree, 1, wx.ALL|wx.EXPAND, 0 )


		self.m_panel7.SetSizer( bSizer6 )
		self.m_panel7.Layout()
		bSizer6.Fit( self.m_panel7 )
		self.m_panel8 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.wire_list = wx.ListCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_HEADER|wx.LC_SMALL_ICON )
		bSizer8.Add( self.wire_list, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( bSizer8 )
		self.m_panel8.Layout()
		bSizer8.Fit( self.m_panel8 )
		self.m_splitter2.SplitVertically( self.m_panel7, self.m_panel8, 0 )
		bSizer5.Add( self.m_splitter2, 1, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer5 )
		self.m_panel5.Layout()
		bSizer5.Fit( self.m_panel5 )
		self.design_builder_book.AddPage( self.m_panel5, u"Design", True, wx.NullBitmap )
		self.m_panel6 = wx.Panel( self.design_builder_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.design_builder_book.AddPage( self.m_panel6, u"Search", False, wx.NullBitmap )

		bSizer4.Add( self.design_builder_book, 1, wx.EXPAND |wx.ALL, 0 )


		self.m_panel2.SetSizer( bSizer4 )
		self.m_panel2.Layout()
		bSizer4.Fit( self.m_panel2 )
		self.m_panel4 = wx.Panel( self.top_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel4.SetMinSize( wx.Size( 100,100 ) )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.design_prop = pg.PropertyGrid(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_BOLD_MODIFIED|wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER)
		bSizer14.Add( self.design_prop, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer14 )
		self.m_panel4.Layout()
		bSizer14.Fit( self.m_panel4 )
		self.top_splitter.SplitHorizontally( self.m_panel2, self.m_panel4, 0 )
		bSizer3.Add( self.top_splitter, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0 )

		self.bt_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.bt_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_hide = wx.BitmapButton( self.bt_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 8,8 ), wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.bt_hide.SetBitmap( wx.NullBitmap )
		bSizer11.Add( self.bt_hide, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

		self.bt_show = wx.BitmapButton( self.bt_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 8,8 ), wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.bt_show.SetBitmap( wx.NullBitmap )
		self.bt_show.Hide()

		bSizer11.Add( self.bt_show, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0 )


		self.bt_panel.SetSizer( bSizer11 )
		self.bt_panel.Layout()
		bSizer11.Fit( self.bt_panel )
		bSizer3.Add( self.bt_panel, 0, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.design_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnTreeSelChange )
		self.wire_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnWireSelect )
		self.bt_hide.Bind( wx.EVT_BUTTON, self.OnShowHideClick )
		self.bt_show.Bind( wx.EVT_BUTTON, self.OnShowHideClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnTreeSelChange( self, event ):
		event.Skip()

	def OnWireSelect( self, event ):
		event.Skip()

	def OnShowHideClick( self, event ):
		event.Skip()


	def top_splitterOnIdle( self, event ):
		self.top_splitter.SetSashPosition( 0 )
		self.top_splitter.Unbind( wx.EVT_IDLE )

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 0 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )


