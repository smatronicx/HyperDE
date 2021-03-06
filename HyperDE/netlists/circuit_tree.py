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

import weakref
import collections

# This class is used to build citcuit tree from netlist for HyperDE

class CktRoot():
    # This class holds information at toplevel of design
    def __init__(self):
        # Initialize
        self.masters = dict()
        self.unattached_inst = list()
        self.topinst = CktMaster("topinst", self)

    def GetTopInstance(self):
        # Get the top instance
        return self.topinst

    def CreateMaster(self, name):
        # Create new master in circuit tree
        if name in self.masters:
            # Master already exists
            raise Exception("Master " + name + " already exists")
        else:
            # Create new master
            self.masters[name] = CktMaster(name, self)
            return self.masters[name]

    def GetMasterByName(self, name):
        # Get master by name
        if name in self.masters:
            return self.masters[name]
        else:
            return None

    def AddUnattached(self, inst):
        # Add unattached instance
        self.unattached_inst.append(inst)

    def AttachMaster(self, master_name, master):
        # Attach master to unattached instance
        remain_unattached = self.unattached_inst[:]
        del self.unattached_inst[:]
        for inst in remain_unattached:
            inst_master = inst.GetMasterName()
            if inst_master == master_name:
                inst.AttachMaster(master)
            else:
                self.AddUnattached(inst)

    #def __del__(self):
    #    print "Deleteing Top"

class CktMaster():
    # This class holds information of a sub-circuit
    def __init__(self, name, root):
        # Initialize
        self.name = name
        self.terms = collections.OrderedDict()
        self.ordered_terms = list()
        self.nets = dict()
        self.instances = collections.OrderedDict()
        self.parameters = collections.OrderedDict()
        self.other_commands = list()
        self.root = weakref.ref(root)

        # Attach instances of this master
        self.root().AttachMaster(name, self)

    def AddTerminal(self, name, type):
        # Add port to the master
        if name in self.terms:
            # Terminal already exists
            raise Exception("Terminal " + name + " already exists")
        else:
            # Find net for terminal
            if name in self.nets:
                net = self.nets[name]
            else:
                net = self.AddNet(name)

            # Add new terminal
            term = self.terms[name] = CktTerminal(name, type, net)
            self.ordered_terms.append(name)
            net.AddTerminal(term)
            return term

    def AddInstance(self, name, master):
        # Add instance to the master
        if name in self.instances:
            # Terminal already exists
            raise Exception("Instance " + name + " already exists")
        else:
            # Add new instance
            self.instances[name] = CktInstance(name, master, self)
            return self.instances[name]

    def AddNet(self, name):
        # Add instance to the master
        if name in self.nets:
            # Terminal already exists
            raise Exception("Net  " + name + " already exists")
        else:
            # Add new instance
            self.nets[name] = CktNet(name)
            return self.nets[name]

    def GetOrderedTerminals(self):
        return self.ordered_terms

    def GetNetByName(self, name):
        # Get net by name
        if name in self.nets:
            return self.nets[name]
        else:
            return None

    def GetInstanceByName(self, name):
        # Get instance by name
        if name in self.instances:
            return self.instances[name]
        else:
            return None

    def GetMasterByName(self, name):
        # Get master by name
        return self.root().GetMasterByName(name)

    def AddUnattached(self, inst):
        # Add unattached instance
        self.root().AddUnattached(inst)

    def GetAllInstance(self):
        # Get all instance in this master
        return self.instances

    def GetAllNets(self):
        # Get all nets in this master
        return self.nets

    def GetAllTerminal(self):
        # Get all terminal in this master
        return self.terms

    def GetTerminalByName(self, name):
        # Get terminal by name
        if name in self.terms:
            return self.terms[name]

        return None

    def GetRoot(self):
        # Get root design
        return self.root()

    #def __del__(self):
    #    print "Deleteing master: "+ self.name

class CktTerminal():
    # This class holds information of a terminal
    def __init__(self, name, type, net):
        # Initialize
        self.name = name
        self.type = type # Can be input, output or ioput
        self.net = weakref.ref(net)

    def GetNet(self):
        # Get the connected net
        return self.net()

    def GetName(self):
        # Get the name of the terminal
        return self.name

    def GetType(self):
        # Get the terminal type
        return self.type

    #def __del__(self):
    #    print "Deleteing term: "+ self.name

class CktNet():
    # This class holds information of a net
    def __init__(self, name):
        # Initialize
        self.name = name
        self.term = None
        self.instances = list()

    def AddTerminal(self, term):
        # Add terminal connected to net
        self.term = weakref.ref(term)

    def GetTerminal(self):
        # Get the terminal of this net
        return self.term

    def AddInstance(self, inst):
        # Add instances connected to net
        self.instances.append(inst)

    def GetName(self):
        # Get the name of the net
        return self.name

    #def __del__(self):
    #    print "Deleteing net: "+ self.name

class CktInstance():
    # This class holds information of an instance
    def __init__(self, name, master_name, parent, icon="subckt"):
        # Initialize
        self.name = name
        self.master_name = master_name
        self.master = None
        self.ordered_terms = list()
        self.parent = weakref.ref(parent)
        self.parameters = collections.OrderedDict()
        self.icon = icon.lower()

        # Check if master exists
        master = self.parent().GetMasterByName(master_name)
        if master is not None:
            self.AttachMaster(master)
        else:
            # Add to unattached list
            self.parent().AddUnattached(self)

    def AttachMaster(self, master):
        # Attached loaded master to instance
        self.master = weakref.ref(master)
        self.master_ordered_terms = self.master().GetOrderedTerminals()

    def AddTerminal(self, name):
        # Add terminal
        self.ordered_terms.append(name)
        # Add net
        net = self.parent().GetNetByName(name)
        if net is None:
            # Create new net in parent
            net = self.parent().AddNet(name)

        net.AddInstance(self)

    def GetMasterName(self):
        # Get the name of the master
        return self.master_name

    def GetMaster(self):
        # Get the master
        if self.master is None:
            return None

        return self.master()

    def GetParent(self):
        # Get the parent
        return self.parent()

    def GetName(self):
        # Get the name of the instance
        return self.name

    def GetIcon(self):
        # Get all root design
        return self.icon

    def GetNetNameOfTerm(self, name):
        # Get net connected to term in parent subckt
        if name in self.master_ordered_terms:
            idx = self.master_ordered_terms.index(name)
            net_name = self.ordered_terms[idx]
            return net_name

        else:
            return None

    #def __del__(self):
    #    print "Deleteing inst: "+ self.name
