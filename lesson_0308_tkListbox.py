#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:29:35 2021

@author: fennieliang
"""

import tkinter as tk

root = tk.Tk()
foods = ['apple', 'banana', 'lemon', 'melon', 'papaya','tomato', 'water melon']
# create a listbox
listbox1 = tk.Listbox(root, selectmode=tk.EXTENDED)
listbox1.pack(padx=10,pady=10)
# use padx and pady to give some space ouside the list box

# insert information to the box
for food in foods:
    listbox1.insert(tk.END, food)

# delete index
#listbox1.delete(0, 1)
root.mainloop()