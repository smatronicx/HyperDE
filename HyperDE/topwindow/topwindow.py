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
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

from functools import partial

from theme import theme_inst as thm
import console as cs

def donothing(tk):
    pass

# This class is used to set main framework for HyperDE

class TopWindow():
    # This class implements main framework

    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if TopWindow.__instance == None:
            raise ValueError("TopWindow is not initialized")
        return TopWindow.__instance

    def __init__(self, master=None, root=None):
        # Initialize
        if TopWindow.__instance != None:
            raise ValueError("The class ""TopWindow"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            #Virtual private constructor
            TopWindow.__instance = self
            #Create widgets
            self._CreateWidgets(master=master, root=root)

    def _CreateWidgets(self, master=None, root=None):
        #Top frame for framework
        self.topframe = thm.Frame(master=master)
        self.topframe.pack(fill=tk.BOTH, expand=tk.YES)

        #Add menus
        self.menubar = tk.Menu()
        root.config(menu=self.menubar)
        self._AddFileMenu()

        c1 = cs.Console(master=self.topframe)

    def _AddFileMenu(self):
        #Add file menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=partial(donothing,tk))
        self.filemenu.add_command(label="Open", command=donothing)
        self.filemenu.add_command(label="Save", command=donothing)
        self.filemenu.add_command(label="Save as...", command=donothing)
        self.filemenu.add_command(label="Close", command=donothing)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=donothing)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
