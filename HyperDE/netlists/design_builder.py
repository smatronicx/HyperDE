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

import wx

from . import design_buildergui as gui
from . import circuit_tree

# This class is used to build design object from netlist for HyperDE

class DesignBuilder(gui.TopPanel):
    # This class implements design object builder

    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if DesignBuilder.__instance is None:
            DesignBuilder()
        return DesignBuilder.__instance

    def __init__(self, parent=None, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(500, 300), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        # Initialize
        if DesignBuilder.__instance is not None:
            raise ValueError("The class ""DesignBuilder"" is defined\n\
            Use getInstance() method to access the class")

        else:
            # Import top windows
            from .. import topwindow as topwindow
            # Virtual private constructor
            DesignBuilder.__instance = self
            #Create widgets
            super(DesignBuilder, self).__init__(parent, id, pos, size, style, name)
            # Variables
            self.netlistpath = None
            self.is_hidden = False
            self.wire_list_map = dict()
            # topwindow path
            self.tw = topwindow.TopWindow.getInstance()
            # Create icon map with design name
            self._CreateIconMap()
            # Fix icon paths
            self._SetIconPath()
            # Add ImageList
            self.wire_list.SetImageList(self.tw.GetIconList(), wx.IMAGE_LIST_SMALL)
            self.design_tree.SetImageList(self.tw.GetIconList())
            # Circuit root
            self.ckt_root = circuit_tree.CktRoot()
            self.ckt_root_name = "topinst"

    def _SetIconPath(self):
        # Fix path for icons
        self.bt_hide.SetBitmap(self.tw.GetIconBitmap("left_arrow"))
        self.bt_show.SetBitmap(self.tw.GetIconBitmap("right_arrow"))

    def _CreateIconMap(self):
        # Create icon map with design name
        self.icon_map = dict()
        self.icon_map["input"] = "terminal_input"
        self.icon_map["output"] = "terminal_output"
        self.icon_map["ioput"] = "terminal_ioput"
        self.icon_map["subckt"] = "ckt_subckt"

    def GetIconIndex(self, name):
        # Get icon index from icon map
        name = name.lower()
        if name in self.icon_map:
            icon_name = self.icon_map[name]
            return self.tw.GetIconIndex(icon_name)

        return -1

    def OnShowHideClick(self, event):
        # Show/Hide the design builder
        if self.is_hidden is False:
            self.bt_show.Show()
            self.bt_hide.Hide()
            self.top_splitter.Hide()
            self.is_hidden = True
            self.bt_panel.Layout()
            panelw, panelh = self.bt_panel.GetSize()
            self.tw.ShowDesignBuilder(show=False, size=panelw)

        else:
            self.bt_show.Hide()
            self.bt_hide.Show()
            self.top_splitter.Show()
            self.is_hidden = False
            self.bt_panel.Layout()
            self.tw.ShowDesignBuilder(show=True)

    def GetCktRoot(self):
        return self.ckt_root

    def OnTreeSelChange(self, event):
        # Update nets and props based on selection
        # Clean list box
        self.wire_list.ClearAll()
        self.wire_list.InsertColumn(0, "name")
        self.wire_list_map.clear()

        # Find tree selection master
        tree_root = self.design_tree.GetRootItem()
        item = event.GetItem()
        if item == tree_root:
            master = self.ckt_root.GetTopInstance()

        else:
            inst = self.design_tree.GetItemData(item)
            master = inst.GetMaster()
            if master is None:
                return

        terms = master.GetAllTerminal()
        term_list = list(sorted(terms.keys()))
        for term in term_list:
            idx = self.wire_list.GetItemCount()
            term_type = terms[term].GetType()
            wire_item = self.wire_list.InsertItem(idx, term,
                self.GetIconIndex(term_type))

            self.wire_list_map[wire_item] = terms[term]
            #self.wire_list.SetItemData(wire_item, terms[term])

        nets = master.GetAllNets()
        net_list = list(sorted(nets.keys()))
        for net in net_list:
            idx = self.wire_list.GetItemCount()
            wire_item = self.wire_list.InsertItem(idx, net,
                self.GetIconIndex("net"))
            #self.wire_list.SetItemData(wire_item, nets[net])
            #print wire_item
            self.wire_list_map[wire_item] = nets[net]

    def BuildTree(self):
        # Build tree for ckt_root
        topinst = self.ckt_root.GetTopInstance()
        tree_root = self.design_tree.AddRoot(self.ckt_root_name,
            self.GetIconIndex("subckt"))
        self._AddTreeNode(tree_root, topinst)

    def _AddTreeNode(self, parent_node, master):
        # Add tree nodes for given master
        insts = master.GetAllInstance()
        for inst in insts:
            inst_name = insts[inst].GetName()
            inst_master_name = insts[inst].GetMasterName()
            inst_icon = insts[inst].GetIcon()

            node_name = inst_name + " {"+inst_master_name+"}"
            childnode = self.design_tree.AppendItem(parent_node,
                node_name, self.GetIconIndex(inst_icon))
            self.design_tree.SetItemData(childnode, insts[inst])

            inst_master = insts[inst].GetMaster()
            if inst_master is not None:
                self._AddTreeNode(childnode, inst_master)

    def OnWireSelect(self, event):
        # Update props based on selection
        item = event.GetItem()
        wire_obj = self.wire_list_map[item.GetId()]
        #print wire_obj.GetName()
        tree_item = self.design_tree.GetSelection()
        #print self.design_tree.GetItemParent(tree_item)
        if isinstance(wire_obj, circuit_tree.CktNet):
            print self.GetHierNetName(tree_item, wire_obj)
        else:
            print self.GetHierTermName(tree_item, wire_obj)

    def GetHierInstName(self, tree_item):
        # Get the complete hierarchical instance name
        tree_root = self.design_tree.GetRootItem()
        if tree_item == tree_root:
            # Root instance
            return ""

        inst_hier_name = ""
        while tree_item != tree_root:
            inst = self.design_tree.GetItemData(tree_item)
            inst_name = inst.GetName()
            inst_hier_name = inst_name + "." + inst_hier_name
            tree_item = self.design_tree.GetItemParent(tree_item)

        # Remove last .
        return inst_hier_name[:-1]

    def GetHierNetName(self, tree_item, net):
        # Get the complete hierarchical net name
        tree_root = self.design_tree.GetRootItem()
        if tree_item == tree_root:
            # Top level net
            return net.GetName()

        # Check if net is terminal
        term = net.GetTerminal()

        if term is None:
            # Net belongs to this hierarchy
            inst_hier_name = self.GetHierInstName(tree_item)
            net_name = inst_hier_name + "." + net.GetName()
            return net_name

        else:
            # Get net from parent
            inst = self.design_tree.GetItemData(tree_item)
            net_name = inst.GetNetNameOfTerm(net.GetName())
            net = inst.GetParent().GetNetByName(net_name)
            tree_item = self.design_tree.GetItemParent(tree_item)
            return self.GetHierNetName(tree_item, net)

        return None

    def GetHierTermName(self, tree_item, term):
        # Get the complete hierarchical term name
        tree_root = self.design_tree.GetRootItem()
        if tree_item == tree_root:
            # Top level
            return None

        # Get instance hierarchical name
        inst_hier_name = self.GetHierInstName(tree_item)
        term_name = inst_hier_name + ":" + term.GetName()
        return term_name
