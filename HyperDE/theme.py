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
    import ScrolledText as tkst
else:
    import tkinter as tk
    import tkinter.scrolledtext as tkst


class Theme():
    # Class to set theme of GUI

    # Singleton instance
    __instance = None

    #Variables
    bg_color = 'light grey' #Background colour

    stdout_fg_color = 'sea green' #Font colour for STDOUT
    stderr_fg_color = 'red' #Font colour for STDERR

    cmd_fg_color = 'blue' #Font colour for console cmd

    @staticmethod
    def getInstance():
        # Static access method
        if Theme.__instance == None:
            Theme()
        return Theme.__instance

    def __init__(self, master=None):
        # Initialize
        if Theme.__instance != None:
            raise ValueError("The class ""Theme"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            Theme.__instance = self


    def Frame(self, master = None):
        # Frame widget
        rtn = tk.Frame(master=master, bg=Theme.bg_color)
        return rtn

    def EntryTransparent(self, master = None):
        #Transparent entry to match back ground
        rtn = tk.Entry(master=master, bg=Theme.bg_color, bd=0)
        return rtn

    def Label(self, master = None):
        #Transparent entry to match back ground
        rtn = tk.Label(master=master, bg=Theme.bg_color)
        return rtn

    def TextTransparent(self, master = None):
        #Transparent entry to match back ground
        rtn = tkst.ScrolledText(master=master, bg=Theme.bg_color, bd=0)
        return rtn

#Create an instace of Theme
theme_inst = Theme.getInstance()
