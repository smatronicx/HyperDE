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
## Class TopFrame
###########################################################################

class TopFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,300 ), wx.DefaultSize )

		self.menubar = wx.MenuBar( 0 )
		self.filemenu = wx.Menu()
		self.filemenunew = wx.MenuItem( self.filemenu, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.filemenu.Append( self.filemenunew )

		self.filemenuexit = wx.MenuItem( self.filemenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.filemenu.Append( self.filemenuexit )

		self.menubar.Append( self.filemenu, u"File" )

		self.aboutmenu = wx.Menu()
		self.menubar.Append( self.aboutmenu, u"About" )

		self.SetMenuBar( self.menubar )

		bsizetop = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SP_3D )
		self.m_splitter2.SetSashGravity( 0.5 )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		self.m_splitter2.SetMinimumPaneSize( 100 )

		self.m_splitter2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel2 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter3 = wx.SplitterWindow( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter3.SetSashGravity( 0.5 )
		self.m_splitter3.Bind( wx.EVT_IDLE, self.m_splitter3OnIdle )
		self.m_splitter3.SetMinimumPaneSize( 100 )

		self.m_panel5 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_button2 = wx.Button( self.m_panel5, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel5.SetSizer( bSizer8 )
		self.m_panel5.Layout()
		bSizer8.Fit( self.m_panel5 )
		self.m_panel6 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self.m_panel6, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button3, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer9 )
		self.m_panel6.Layout()
		bSizer9.Fit( self.m_panel6 )
		self.m_splitter3.SplitVertically( self.m_panel5, self.m_panel6, 250 )
		bSizer6.Add( self.m_splitter3, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer6 )
		self.m_panel2.Layout()
		bSizer6.Fit( self.m_panel2 )
		self.m_panel1 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_splitter2.SplitHorizontally( self.m_panel2, self.m_panel1, 350 )
		bsizetop.Add( self.m_splitter2, 1, wx.EXPAND, 5 )


		self.SetSizer( bsizetop )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnClickFileMenuNew, id = self.filemenunew.GetId() )
		self.Bind( wx.EVT_MENU, self.OnClickFileMenuExit, id = self.filemenuexit.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClickFileMenuNew( self, event ):
		event.Skip()

	def OnClickFileMenuExit( self, event ):
		event.Skip()

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 350 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )

	def m_splitter3OnIdle( self, event ):
		self.m_splitter3.SetSashPosition( 250 )
		self.m_splitter3.Unbind( wx.EVT_IDLE )


