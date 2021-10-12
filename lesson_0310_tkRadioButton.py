#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:43:22 2021

@author: fennieliang
"""

import tkinter as tk

main = tk.Tk() #declare a main window

main.title("My Phthon Window")


#  add label to the window
# incase the text is too close to the radio buttons, add height to the attribute
w = tk.Label(main, text='please select one from the followings:', bg="#949595").pack()

#  add radio buttons in a frame to the window

# Tkinter string variable
# able to store any string value
v = tk.StringVar(main, "1")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
        "RadioButton 2" : "2",
        "RadioButton 3" : "3",
        "RadioButton 4" : "4",
        "RadioButton 5" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    tk.Radiobutton(main, text = text, variable = v,
        value = value, bg="#954BF8").pack(side = "top", ipady = 5)


main.mainloop()#mainloop is for window to active