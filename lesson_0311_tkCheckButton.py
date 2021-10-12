#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:19:58 2021

@author: fennieliang
"""

import tkinter as tk

main = tk.Tk() #declare a main window

main.title("My Phthon Window")


#  add checkbox to the window
var1 = tk.IntVar()
tk.Checkbutton(main, text='teacher', variable=var1).pack()
var2 = tk.IntVar()
tk.Checkbutton(main, text='student', variable=var2).pack()

main.mainloop()#mainloop is for window to active