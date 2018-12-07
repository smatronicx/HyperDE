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

from code import InteractiveConsole
from imp import new_module
from theme import theme_inst as thm

# This class implements the integrated console
# It is deviced into two parts, one for GUI and other for code execution

class _Console(InteractiveConsole):
    # This class implements code execution

    def __init__(self, names=None):
        # Initialize
        names = names or {}
        names['console'] = self
        InteractiveConsole.__init__(self, names)
        self.superspace = new_module('superspace')

    def enter(self, source):
        # Execute the code
        source = self.preprocess(source)
        self.runcode(source)

    @staticmethod
    def preprocess(source):
        # Function to preprocess the code
        return source

class _RedirectText(object):
    # This class redirect STD outputs to GUI textbox

    def __init__(self, textbox):
        # Initialize
        self.output = textbox

    def write(self, string):
        # Write to textbox
        self.output.insert(tk.END, string)

class Console():
    # This class implements GUI

    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if Console.__instance == None:
            #Console()
            raise ValueError("Console is not initialized")
        return Console.__instance

    def __init__(self, master=None):
        # Initialize
        if Console.__instance != None:
            raise ValueError("The class ""Console"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            Console.__instance = self
            #Top frame for console
            self.topframe = thm.Frame(master=master)
            self.topframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

            self.txt = tk.StringVar()
            self.rootEntry = tk.Entry(self.topframe, textvariable=self.txt)
            self.rootEntry.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
            #self.rootEntry.bind("<Return>", self.cycle_text)
            self.rootText = tk.Text(self.topframe)
            self.rootText.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
            redir = _RedirectText(self.rootText)
            sys.stdout = redir
            sys.stderr = redir
            #self.rootText.bind("<Insert>", self.insert_all)
            self.newList = []
            self.console = _Console()
