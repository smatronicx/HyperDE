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

import sys
import wx

import design_buildergui as gui
import topwindow
import circuit_tree

# This class is used to build design object from netlist for HyperDE

class DesignBuilder(gui.TopPanel):
    # This class implements design object builder

    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if DesignBuilder.__instance == None:
            DesignBuilder()
        return DesignBuilder.__instance

    def __init__(self, parent=None, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        # Initialize
        if DesignBuilder.__instance != None:
            raise ValueError("The class ""DesignBuilder"" is defined\n\
            Use getInstance() method to access the class")

        else:
            # Virtual private constructor
            DesignBuilder.__instance = self
            #Create widgets
            super(DesignBuilder, self).__init__(parent=parent)
            # Variables
            self.netlistpath = None
            self.is_hidden = False
            # Fix icon paths
            self._SetIconPath()
            # Circuit root
            self.ckt_root = circuit_tree.CktRoot()
            self.ckt_root_name = "topinst"

    def _SetIconPath(self):
        # Fix path for icons
        self.bt_hide.SetBitmap(wx.Bitmap(homepath + "/res/left_arrow.png", wx.BITMAP_TYPE_ANY))
        self.bt_show.SetBitmap(wx.Bitmap(homepath + "/res/right_arrow.png", wx.BITMAP_TYPE_ANY))

    def OnShowHideClick(self, event):
        # Show/Hide the design builder
        tw = topwindow.TopWindow.getInstance()
        if self.is_hidden == False:
            self.bt_show.Show()
            self.bt_hide.Hide()
            self.top_splitter.Hide()
            self.is_hidden = True
            self.bt_panel.Layout()
            panelw,panelh = self.bt_panel.GetSize()
            tw.ShowDesignBuilder(show=False, size=panelw)

        else:
            self.bt_show.Hide()
            self.bt_hide.Show()
            self.top_splitter.Show()
            self.is_hidden = False
            self.bt_panel.Layout()
            tw.ShowDesignBuilder(show=True)

    def GetCktRoot(self):
        return self.ckt_root

    def OnClick(self, event):
        print event

    def OnChange(self, event):
        root1 = self.design_tree.GetRootItem()
        item = event.GetItem()
        if item == root1:
            print "Root"

        master = self.design_tree.GetItemData(item)
        terms = master.GetAllTerminal()
        term_list = list(sorted(terms.keys()))
        for term in term_list:
            print "t:" + term

        # Nets
        nets = master.GetAllNets()
        net_list = list(sorted(nets.keys()))
        for net in net_list:
            print "n:" + net

    def BuildTree(self):
        # Build tree for ckt_root
        topinst = self.ckt_root.GetTopInstance()
        tree_root = self.design_tree.AddRoot(self.ckt_root_name)
        self.AddTreeNode(tree_root, topinst)
        pass

    def AddTreeNode(self, parent_node, master):
        # Add tree nodes for given master
        insts = master.GetAllInstance()
        for inst in insts:
            self.design_tree.SetItemData(parent_node, insts[inst])

            inst_name = insts[inst].GetName()
            inst_master_name = insts[inst].GetMasterName()

            node_name = inst_name + " {"+inst_master_name+"}"
            childnode = self.design_tree.AppendItem(parent_node,node_name)

            inst_master = insts[inst].GetMaster()
            if inst_master != None:
                self.AddTreeNode(childnode, inst_master)
