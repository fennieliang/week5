#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:04:49 2021

@author: fennieliang
"""

import tkinter as tk

main = tk.Tk() #declare a main window

main.title("My Phthon Window")

#  add labels in a frame to the window
frame1 = tk.Label(main, bg='#949595')
frame1.pack()
tk.Label(frame1, text='Full Name').grid(row=0, column=0)
#use padx and pady to give space between each label and entry
tk.Label(frame1, text='Email').grid(row=1, column=0)
tk.Label(frame1, text='Password').grid(row=2, column=0)
#name_Tf = tk.Entry(frame1)
#name_Tf.grid(row=0, column=1)
tk.Entry(frame1).grid(row=0, column=1)
tk.Entry(frame1).grid(row=1, column=1)
tk.Entry(frame1, show="*").grid(row=2, column=1)

main.mainloop()#mainloop is for window to active