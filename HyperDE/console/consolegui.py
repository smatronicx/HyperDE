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

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.out_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_BESTWRAP|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH|wx.TE_RICH2 )
		bSizer7.Add( self.out_text, 1, wx.ALL|wx.EXPAND, 0 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.in_label = wx.StaticText( self, wx.ID_ANY, u">>>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.in_label.Wrap( -1 )

		bSizer19.Add( self.in_label, 0, wx.ALIGN_BOTTOM|wx.RIGHT, 5 )

		self.in_indent = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.in_indent.Wrap( -1 )

		bSizer19.Add( self.in_indent, 0, wx.ALL, 0 )

		self.in_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.TE_RICH|wx.TE_RICH2|wx.BORDER_NONE|wx.WANTS_CHARS )
		bSizer19.Add( self.in_text, 1, wx.ALL|wx.EXPAND, 0 )


		bSizer7.Add( bSizer19, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		# Connect Events
		self.in_text.Bind( wx.EVT_KEY_DOWN, self._OnKeyDown )
		self.in_text.Bind( wx.EVT_TEXT_ENTER, self._ParseInput )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnKeyDown( self, event ):
		event.Skip()

	def _ParseInput( self, event ):
		event.Skip()


