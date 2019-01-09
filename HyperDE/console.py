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

    def __init__(self, textbox, bg='white', fg='black', tag='tag'):
        # Initialize
        self.output = textbox
        self.bg = bg
        self.fg = fg
        self.tag = tag

    def write(self, string):
        # Write to textbox
        self.output["state"] = tk.NORMAL
        start_idx = self.output.index(tk.END+"-1c")
        self.output.insert(tk.END, string)
        end_idx = self.output.index(tk.END+"-1c")
        #Set text colour
        self.output.tag_add(self.tag, start_idx, end_idx)
        self.output.tag_config(self.tag, foreground=self.fg,\
            background=self.bg)
        self.output["state"] = tk.DISABLED
        self.output.see(tk.END)

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
            #Create widgets
            self._CreateWidgets(master=master)

            #Redirect STDOUT/STDERR to console
            sys.stdout = _RedirectText(self.out_text, fg=thm.stdout_fg_color,
                bg=thm.bg_color, tag='stdout')
            sys.stderr = _RedirectText(self.out_text, fg=thm.stderr_fg_color,
                bg=thm.bg_color, tag='stderr')

            self.console = _Console() #Console class
            self.cmd_history = [] #Variable to hold command history
            self.cmd_index = -1 # The current index in commmad history

            self.is_multiline_cmd = 0 # 1 if command is multiple lines
            self.multiline_cmd = "" # Variable to hold multiple lines of command

    def _CreateWidgets(self, master=None):
        #Create GUI for console
        #Top frame for console
        self.topframe = thm.Frame(master=master)
        self.topframe.pack(fill=tk.BOTH, expand=tk.YES)

        #Output widget
        self.out_text = thm.TextTransparent(master=self.topframe)
        self.out_text.pack(fill=tk.BOTH, expand=tk.YES)
        self.out_text["state"] = tk.DISABLED

        #Input widget
        self.in_frame = thm.Frame(master=self.topframe)
        self.in_frame.pack(fill=tk.X, expand=tk.NO)
        self.in_label = thm.Label(self.in_frame)
        self.in_label["text"] = ">>>"
        self.in_label.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.NO)

        self.in_indent = thm.Label(self.in_frame)
        self.in_indent["text"] = ""
        self.in_indent.pack(side=tk.LEFT, fill=tk.NONE, expand=tk.NO)
        self.in_indent_char = "...." # Display character
        self.in_indent_space = "    " # Actual spaces

        self.in_text = tk.StringVar()
        self.in_entry = thm.EntryTransparent(master=self.in_frame)
        self.in_entry["textvariable"] = self.in_text
        self.in_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.in_entry.bind("<Return>", self._ParseInput)
        self.in_entry.bind("<Up>", self._ShowPreviousCmd)
        self.in_entry.bind("<Down>", self._ShowNextCmd)
        self.in_entry.bind("<Tab>", self._AddTab)
        self.in_entry.bind("<BackSpace>", self._RemoveTab)

    def _ParseInput(self, arg=None):
        # Parse the input text and pass it to console
        # Get text from text box
        t = self.in_text.get()

        if self.cmd_index > len(self.cmd_history)-1:
            # At max index then increament it
            self.cmd_index += 1

        # Add command in history
        self.cmd_history.append(t)

        # Display command in textbox
        self.out_text["state"] = tk.NORMAL
        start_idx = self.out_text.index(tk.END+"-1c")
        self.out_text.insert(tk.END, self.in_indent["text"])
        self.out_text.insert(tk.END, t+"\n")
        end_idx = self.out_text.index(tk.END+"-1c")
        self.out_text.tag_add("cmd", start_idx, end_idx)
        self.out_text.tag_config("cmd", foreground=thm.cmd_fg_color)
        self.out_text["state"] = tk.DISABLED
        self.out_text.see(tk.END)

        # Handle multiple line command
        t=t.strip()
        if t[-1:] == ":":
            # Got multiple line command
            if self.is_multiline_cmd == 0:
                # Start multiple line command
                self.is_multiline_cmd = 1

        if self.is_multiline_cmd == 1:
            # Check if got blank line
            if len(t) == 0:
                # Run command
                self.console.runcode(self.multiline_cmd)
                self.multiline_cmd = ""
                self.in_indent["text"]  = ""

            else:
                # Add command
                in_tabs = self.in_indent["text"]
                in_tabs = in_tabs.replace(self.in_indent_char,
                    self.in_indent_space)
                self.multiline_cmd += in_tabs
                self.multiline_cmd += t
                self.multiline_cmd +='\n'

                if t[-1:] == ":":
                    # Add indent
                    self.in_indent["text"] += self.in_indent_char

        else:
            self.console.runcode(t)

        self.in_text.set("")

    def _ShowNextCmd(self, arg=None):
        # Put next command from history
        if self.cmd_index == -1:
            # If history is called first time
            return

        # Max index of history
        max_idx = len(self.cmd_history)-1

        self.cmd_index += 1

        if self.cmd_index > max_idx:
            self.cmd_index = max_idx + 1
            self.in_text.set("")
            return

        # Set command in entry
        self.in_text.set(self.cmd_history[self.cmd_index])
        self.in_entry.icursor(tk.END)

    def _ShowPreviousCmd(self, arg=None):
        # Put next command from history

        if len(self.cmd_history) == 0:
            # No commands in history
            return

        if self.cmd_index == -1:
            # If history is called first time
            self.cmd_index = len(self.cmd_history)-1
        else:
            self.cmd_index -= 1

        if self.cmd_index < 0:
            self.cmd_index = 0

        # Set command in entry
        self.in_text.set(self.cmd_history[self.cmd_index])
        self.in_entry.icursor(tk.END)

    def _AddTab(self, arg=None):
        # Add tab character in entry
        if self.in_entry.index(tk.INSERT) == 0:
            # Tab pressed at starting of line
            self.in_indent["text"] += self.in_indent_char
            return 'break'

    def _RemoveTab(self, arg=None):
        # Remove tab character in entry
        if self.in_entry.index(tk.INSERT) == 0:
            # Backspace pressed at starting of line
            self.in_indent["text"] = \
                self.in_indent["text"][:-1*len(self.in_indent_char)]
            return 'break'

# Methods for top namespace
