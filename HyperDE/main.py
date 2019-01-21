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

#wv.wv_canvas.test()
#import console as cs
#import topwindow.topwindow as tw

#import cframe as cf

#root = tk.Tk()
#root.geometry('500x500')
#frame = tk.Frame(master=root, bg='white')
#frame.pack(fill=tk.BOTH, expand=tk.YES)
#app = wv.wv_canvas.WaveCanvas(master=frame)

#c1 = cs.Console(master=frame)
#t1 = tw.TopWindow(master=frame, root=root)

#root = tk.Tk()
#root.wm_geometry("400x300+0+0")

#cf1 = cf.CollapsibleFrame(root, text ="Frame1", interior_padx=6)
#cf1.pack()

#for i in range(3):
#    tk.Button(cf1.interior, text="button %s"%i).pack(side=tk.LEFT)

#cf1.update_width()

#root.mainloop()

import topwindow.topwindow as topwin
import wx as wx


app = wx.App(False)
#frame = wxpy.MyFrame1(parent=None)
frame = topwin.TopWindow(parent=None)

frame.Show()
frame.test()
app.MainLoop()
