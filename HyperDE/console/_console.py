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
import wx

from code import InteractiveConsole
from imp import new_module

import consolegui as gui

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

    def __init__(self, textbox, fg='black'):
        # Initialize
        self.output = textbox
        self.fg = fg

    def write(self, string):
        # Write to textbox
        old_style = self.output.GetDefaultStyle()
        self.output.SetDefaultStyle(wx.TextAttr(self.fg))
        self.output.AppendText(string)
        self.output.SetDefaultStyle(old_style)

class Console(gui.TopPanel):
    # This class implements GUI

    # Singleton instance
    __instance = None
    stdout_fg_color = wx.GREEN
    stderr_fg_color = wx.RED
    cmd_fg_color = wx.BLUE

    @staticmethod
    def getInstance():
        # Static access method
        if Console.__instance == None:
            #Console()
            raise ValueError("Console is not initialized")
        return Console.__instance

    def __init__(self, parent=None, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString):
        # Initialize
        if Console.__instance != None:
            raise ValueError("The class ""Console"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            Console.__instance = self
            #Create widgets
            super(Console, self).__init__(parent=parent)
            # Fix colour
            Console.stdout_fg_color = wx.ColourDatabase().Find("FOREST GREEN")

            #Redirect STDOUT/STDERR to console
            #sys.stdout = _RedirectText(self.out_text, fg=Console.stdout_fg_color)
            #sys.stderr = _RedirectText(self.out_text, fg=Console.stderr_fg_color)

            self.console = _Console() #Console class
            self.cmd_history = [] #Variable to hold command history
            self.cmd_index = -1 # The current index in commmad history

            self.is_multiline_cmd = 0 # 1 if command is multiple lines
            self.multiline_cmd = "" # Variable to hold multiple lines of command
            self.in_indent_char = "...." # Display character
            self.in_indent_space = "    " # Actual spaces

    def _ParseInput(self, arg=None):
        # Parse the input text and pass it to console
        # Get text from text box
        t = self.in_text.GetValue()

        if self.cmd_index > len(self.cmd_history)-1:
            # At max index then increament it
            self.cmd_index += 1

        # Add command in history
        self.cmd_history.append(t)

        # Display command in textbox
        in_tabs = self.in_indent.GetLabelText()
        in_tabs = in_tabs.replace(self.in_indent_char,
            self.in_indent_space)
        self.out_text.SetDefaultStyle(wx.TextAttr(Console.cmd_fg_color))
        self.out_text.AppendText(in_tabs+t+"\n")

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
                self.in_indent.SetLabelText(wx.EmptyString)
                self.Layout()

            else:
                # Add command
                self.multiline_cmd += in_tabs
                self.multiline_cmd += t
                self.multiline_cmd +='\n'

                if t[-1:] == ":":
                    # Add indent
                    self._AddTab(force=1)

        else:
            self.console.runcode(t)

        self.in_text.SetValue(wx.EmptyString)

    def _OnKeyDown(self, event):
        # Parse the input key and pass it to console
        # Get the key
        keycode = event.GetKeyCode()
        controlDown = event.CmdDown()
        altDown = event.AltDown()
        shiftDown = event.ShiftDown()

        # Act based on keys
        if keycode == wx.WXK_UP:
            self._ShowPreviousCmd()
        elif keycode == wx.WXK_DOWN:
            self._ShowNextCmd()
        elif keycode == wx.WXK_TAB:
            if self._AddTab() == 1:
                return
        elif keycode == wx.WXK_BACK:
            if self._RemoveTab() == 1:
                return

        event.Skip()

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
            self.in_text.SetValue("")
            return

        # Set command in entry
        self.in_text.SetValue(self.cmd_history[self.cmd_index])
        self.in_text.SetInsertionPointEnd()

    def _ShowPreviousCmd(self, arg=None):
        # Put previous command from history

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
        self.in_text.SetValue(self.cmd_history[self.cmd_index])
        self.in_text.SetInsertionPointEnd()

    def _AddTab(self, force=0,arg=None):
        # Add tab character in entry
        if self.in_text.GetInsertionPoint() == 0:
            force = 1

        if force == 1:
            # Tab pressed at starting of line
            t = self.in_indent.GetLabelText()
            self.in_indent.SetLabelText(t + self.in_indent_char)
            self.Layout()
            return 1

    def _RemoveTab(self, arg=None):
        # Remove tab character in entry
        if self.in_text.GetInsertionPoint() == 0:
            # Backspace pressed at starting of line
            t = self.in_indent.GetLabelText()
            self.in_indent.SetLabelText(t[:-1*len(self.in_indent_char)])
            self.Layout()
            return 1

    def ExecConsoleCode(self, string):
        # Run code in console
        self.console.runcode(string)
