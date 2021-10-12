#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:44:58 2021

@author: fennieliang
"""
import tkinter as tk

main = tk.Tk() #declare a main window

main.title("My Phthon Window")

#first time use to give an area of the tk window
main.geometry('300x300')

#tk.Menubutton is to display text for users to read
menubutton1=tk.Menubutton(main, text = 'Edit')

#tk.Menu is to produce conent inside the dropdown menu
menu_content = tk.Menu(menubutton1)

#place the menubutton1 on the top of the tk window
menubutton1.pack(side='top')

menubutton1.config(menu=menu_content)

#a list of function can be added here
menu_content.add_command(label = 'copy')
menu_content.add_command(label = 'paste')

main.mainloop()


