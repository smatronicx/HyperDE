
if False:
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
if False:
    import HyperDE.netlists.circuit_tree as ct

    def build_des(root):

        m1 = root.GetTopInstance()
        i1 = m1.AddInstance("Xbuff1", "buffer")
        t1 = i1.AddTerminal("a_")
        t1 = i1.AddTerminal("a")
        i1 = m1.AddInstance("Xbuff2", "buffer")
        t1 = i1.AddTerminal("b_")
        t1 = i1.AddTerminal("b")
        i1 = m1.AddInstance("Xnand1", "nand")
        t1 = i1.AddTerminal("a")
        t1 = i1.AddTerminal("b")
        t1 = i1.AddTerminal("out")

        m1 = root.CreateMaster("buffer")
        t1 = m1.AddTerminal("in", "input")
        t1 = m1.AddTerminal("out", "input")
        i1 = m1.AddInstance("Xinv1", "inverter")
        t1 = i1.AddTerminal("in")
        t1 = i1.AddTerminal("mid")
        i1 = m1.AddInstance("Xinv2", "inverter")
        t1 = i1.AddTerminal("mid")
        t1 = i1.AddTerminal("out")

        m1 = root.CreateMaster("inverter")
        t1 = m1.AddTerminal("in", "input")
        t1 = m1.AddTerminal("out", "input")
        i1 = m1.AddInstance("Mn1", "N")
        t1 = i1.AddTerminal("out")
        t1 = i1.AddTerminal("in")
        t1 = i1.AddTerminal("0")
        t1 = i1.AddTerminal("0")
        i1 = m1.AddInstance("Mp1", "P")
        t1 = i1.AddTerminal("out")
        t1 = i1.AddTerminal("in")
        t1 = i1.AddTerminal("vdd")
        t1 = i1.AddTerminal("vdd")

    #m1 = root.CreateMaster("inverter")

    def print_all_inst(master, indt):
        # Terms
        terms = master.GetAllTerminal()
        term_list = list(sorted(terms.keys()))
        for term in term_list:
            print indt + "t:" + term

        # Nets
        nets = master.GetAllNets()
        net_list = list(sorted(nets.keys()))
        for net in net_list:
            print indt + "n:" + net

        # Inst
        insts = master.GetAllInstance()
        for inst in insts:
            inst_name = insts[inst].GetName()
            inst_master_name = insts[inst].GetMasterName()
            print indt + inst_name+ " " + inst_master_name
            inst_master = insts[inst].GetMaster()
            if inst_master != None:
                print_all_inst(inst_master, indt+"  ")

    def tree_all_inst(master, rootnode, treeCtrl):
        # Terms
        terms = master.GetAllTerminal()
        term_list = list(sorted(terms.keys()))
        for term in term_list:
            #print indt + "t:" + term
            pass

        # Nets
        nets = master.GetAllNets()
        net_list = list(sorted(nets.keys()))
        for net in net_list:
            #print indt + "n:" + net
            pass

        #master_data = wx.TreeItemData(master)
        treeCtrl.SetItemData(rootnode, master)
        # Inst
        insts = master.GetAllInstance()
        for inst in insts:
            inst_name = insts[inst].GetName()
            inst_master_name = insts[inst].GetMasterName()

            childnode = treeCtrl.AppendItem(rootnode,inst_name+" {"+inst_master_name+"}")

            #print indt + inst_name+ " " + inst_master_name
            inst_master = insts[inst].GetMaster()
            if inst_master != None:
                tree_all_inst(inst_master, childnode, treeCtrl)


    #m1 = root.GetTopInstance()
    #print_all_inst(m1,"")

    #i1 = m1.GetInstanceByName("Xbuff1")
    #m2 = i1.GetMaster()

    #n1 = m2.GetNetByName("mid")

    #print n1.GetName()

if False:

    import HyperDE.topwindow as topwin
    import wx as wx

    import sys
    import os.path

    #import netlists.readers.read_spectre as n1
    import HyperDE.netlists

    app = wx.App(False)
    frame = wx.Frame(parent=None)
    #frame = topwin.TopWindow(parent=None)
    import HyperDE.waveview as waveview

    bsizer_waveview = wx.BoxSizer( wx.VERTICAL )
    waveview_panel = waveview.WaveView( frame, wx.ID_ANY, wx.DefaultPosition, wx.Size(500,300), wx.TAB_TRAVERSAL )
    bsizer_waveview.Add( waveview_panel, 1, wx.EXPAND |wx.ALL, 0 )
    frame.SetSizer( bsizer_waveview )
    frame.Layout()
    bsizer_waveview.Fit( frame )

    frame.Show()

    #treeCtrl = netlists.DesignBuilder.getInstance().GetTree()
    #rootId = treeCtrl.AddRoot("Root")
    #tree_all_inst(m1,rootId, treeCtrl)

    #ckt_root = netlists.DesignBuilder.getInstance().GetCktRoot()
    #build_des(ckt_root)
    #netlists.DesignBuilder.getInstance().BuildTree()

    #treeCtrl.AppendItem(rootId, "Node 1")
    #child2Id = treeCtrl.AppendItem(rootId, "Node 2")
    #treeCtrl.AppendItem(child2Id, "Child of node 2")
    #treeCtrl.AppendItem(rootId, "Node 3")

    #n1.ReadSpecterNetlist()

    #with open('../../netlist.scs') as f:
    #    for line in f:
    #        print line

    #treeCtrl.DeleteAllItems()
    app.MainLoop()

if True:
    import HyperDE.cppmodules.wavefunc as wf
    import numpy as np
    import ctypes

    import importlib
    pkg = __name__.rpartition('.')[0]
    mname = '.'.join((pkg, '_wavefunc')).lstrip('.')
    try:
        _wavefunc = importlib.import_module(mname)
    except ImportError:
        _wavefunc = importlib.import_module('_wavefunc')

    #print wf.cos_func(0)
    #print wf.cos_func("s")
    x=np.array([1.1, 2.2]).astype(np.double)
    y=np.array([2.1, 3.2]).astype(np.double)
    y0 = np.array([0.0]).astype(np.double)
    wfc = wf.WaveFunc()
    print wfc.FindYatX(x, y, y0, x[0], 0)
    print y0
    print wfc.FindXatY(x, y, y0, 3.1, 2)
    print y0

    print wfc.FindNearestIndex(x, 1.2,0)
    print wfc.FindNearestIndex(x, 2.2,0)
    print wfc.FindNearestIndex(x, 3.2,0)
    print wfc.FindNearestIndex(x, 2.2,1)
    print wfc.FindNearestIndex(x, 2.2,2)
