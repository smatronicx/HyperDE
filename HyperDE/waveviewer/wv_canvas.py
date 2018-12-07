#Import modules
import sys

if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

from functools import partial
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class WaveCanvas(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.createWidgets()

    def createWidgets(self):
        #self.hi_there = tk.Button(self)
        #self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        #self.hi_there.pack()
        f = Figure(facecolor='black')
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        a = f.add_subplot(111)

        a.grid(True)

        x_list = [0, 1, 2, 3, 4, 5]
        y_list = [0, 1, 4, 9, 16, 25]
        y_list2 = [1, 2, 5, 10, 17, 26]

        a1 = a.plot(x_list,y_list)
        a2 = a.plot(x_list,y_list2)

        print a1
        print a2
        a.set_xlabel('time [s]', color='white')
        a.set_ylabel('signal', color='white')

        a.set_facecolor('black')

        a.tick_params(labelcolor='white')

        a.set_frame_on(True)
        #a.margins(0)
        #a.set_xlim(1,3)
        #a.set_ylim(5,6)

        #toolbar = NavigationToolbar2TkAgg(canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def say_hi(self):
        print("hi there, everyone!")
