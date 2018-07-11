# -*- coding: utf-8 -*-

'''effective Voltage and signal history in TKinter window'''

from __future__ import print_function, division, unicode_literals
from __future__ import absolute_import

import sys, time, numpy as np

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
if sys.version_info[0] < 3:
  import Tkinter as Tk
  import tkMessageBox as mbox
  from tkFileDialog import asksaveasfilename
else:
  import tkinter as Tk
  from tkinter import messagebox as mbox
  from tkinter.filedialog import asksaveasfilename

import matplotlib.pyplot as plt, matplotlib.animation as anim

# import XYPlotter class
from .XYPlotter import *

def mpXYPlotter(Q, conf,  
                name='Voltage', cmdQ=None):
  '''effective Voltage of data passed via multiprocessing.Queue
    Args:
      conf: picoConfig object
      Q:    multiprocessing.Queue()   
  '''

  interval = conf['Interval']
  WaitTime = interval * 1000 # in ms

  # Generator to provide data to animation
  def yieldEvt_fromQ():
# random consumer of Buffer Manager, receives an event copy 
   # via a Queue from package mutiprocessing
    cnt = 0
    lagging = False

    while True:
      T0 = time.time()
      if not Q.empty():
        data = Q.get()
        if type(data) != np.ndarray:
          break # received end event
        cnt+=1
        yield (cnt, data)
      else:
        yield None # send empty event if no new data

# guarantee correct timing 
      dtcor = interval - time.time() + T0
      if dtcor > 0. :  
        time.sleep(dtcor) 
        if lagging: 
          LblStatus.config(text='')
          lagging=False
      else:
        lagging=True
        LblStatus.config(text='! lagging !', fg='red')

    # print('*==* yieldEvt_fromQ: received END event')          
    sys.exit()

  def cmdResume():
    cmdQ.put('R')
    buttonP.config(text='Pause', fg='blue', state=Tk.NORMAL)
    buttonR.config(state=Tk.DISABLED)

  def cmdPause():
    cmdQ.put('P')
    buttonP.config(text='paused', fg='grey', state=Tk.DISABLED)
    buttonR.config(state=Tk.NORMAL)
    

  def cmdEnd():
    cmdQ.put('E')

  def cmdSave():
    cmdPause()
    try:
      filename = asksaveasfilename(initialdir='.', initialfile='DGraphs.png', 
               title='select file name')
      figXY.savefig(filename) 
    except: 
      pass
 
# ------- executable part -------- 
#  print(' -> mpXYPlotter starting')

  XY = XYPlotter(conf, name)
  figXY = XY.fig

# generate a simple window for graphics display as a tk.DrawingArea
  root = Tk.Tk()
  root.wm_title("Data Graphs")

# handle destruction of top-level window
  def _delete_window():
    if mbox.askokcancel("Quit", "Really destroy  main window ?"):
       print("Deleting main window")
       root.destroy()
  root.protocol("WM_DELETE_WINDOW", _delete_window)


# Comand buttons
  frame = Tk.Frame(master=root)
  frame.grid(row=0, column=8)
  frame.pack(padx=5, side=Tk.BOTTOM)

  buttonE = Tk.Button(frame, text='End', fg='red', command=cmdEnd)
  buttonE.grid(row=0, column=8)

  blank = Tk.Label(frame, width=7, text="")
  blank.grid(row=0, column=7)

  clock = Tk.Label(frame)
  clock.grid(row=0, column=5)

  buttonSv = Tk.Button(frame,width=8,text='save',fg='purple', command=cmdSave)
  buttonSv.grid(row=0, column=4)

  buttonP = Tk.Button(frame,width=8,text='Pause',fg='blue', command=cmdPause)
  buttonP.grid(row=0, column=3)

  buttonR = Tk.Button(frame,width=8,text='Resume',fg='blue', command=cmdResume)
  buttonR.grid(row=0, column=2)
  buttonR.config(state=Tk.DISABLED)

  LblStatus = Tk.Label(frame, width=13, text="")
  LblStatus.grid(row=0, column=0)

  canvas = FigureCanvasTkAgg(figXY, master=root)
  canvas.draw()
  canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
  canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

# set up matplotlib animation
  tw = max(WaitTime-200., 0.5) # smaller than WaitTime to allow for processing
  DGAnim = anim.FuncAnimation(figXY, XY, yieldEvt_fromQ,
                         interval = tw, init_func = XY.init,
                         blit=True, fargs=None, repeat=True, save_count=None)
                       # save_count=None is a (temporary) work-around 
                       #     to fix memory leak in animate
  Tk.mainloop()
  print('*==* mpXYPlotter: terminating')
  sys.exit()
