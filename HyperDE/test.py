from functools import partial

import matplotlib as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

import waveviewer as wv

from code import InteractiveConsole
from imp import new_module

class Console(InteractiveConsole):

    def __init__(self, names=None):
        names = names or {}
        names['console'] = self
        InteractiveConsole.__init__(self, names)
        self.superspace = new_module('superspace')

    def enter(self, source):
        source = self.preprocess(source)
        self.runcode(source)

    @staticmethod
    def preprocess(source):
        return source

console = Console()

from itertools import cycle

from StringIO import StringIO  # Python2
from io import StringIO  # Python3

old_stdout = sys.stdout

class RedirectText(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, text_ctrl):
        """Constructor"""
        self.output = text_ctrl

    #----------------------------------------------------------------------
    def write(self, string):
        """"""
        self.output.insert(tk.END, string)

class App(tk.Frame):
    def __init__(self, textList, console, master=None):
        tk.Frame.__init__(self, master)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        #self.textiter = cycle(textList)
        self.txt = tk.StringVar()
        self.rootEntry = tk.Entry(self, textvariable=self.txt)
        self.rootEntry.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.rootEntry.bind("<Return>", self.cycle_text)
        self.rootText = tk.Text(self)
        self.rootText.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        redir = RedirectText(self.rootText)
        sys.stdout = redir
        sys.stderr = redir
        #self.rootText.bind("<Insert>", self.insert_all)
        self.newList = []
        self.console = console


    def cycle_text(self, arg=None):
        #t = self.textiter.next()
        t = self.txt.get()
        self.rootText.insert("end", t+"\n")
        self.console.runcode(t)
        self.txt.set("")
        #self.newList.append(self.rootText.get("end - 2 chars linestart", "end - 1 chars"))

    def insert_all(self, arg):
        self.rootText.insert("end", "".join([s.strip() for s in self.newList]))


#wv.wv_canvas.test()
import console as cs
import theme as thm

root = tk.Tk()
root.geometry('500x500')
frame = tk.Frame(master=root, bg='white')
#frame = tk.Frame(master=root, bg='black')
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
#app = wv.wv_canvas.WaveCanvas(master=frame)

#textList = ["Line 1", "Line 2", "Line 3"]
#ent = App(textList, console, master=frame)

#c2 = cs.Console.getInstance()
c1 = cs.Console(master=frame)
c2 = cs.Console.getInstance()

import ctypes
import io
import os, sys

#os.system('echo and this is from echo')
print c1
print c2

root.mainloop()
