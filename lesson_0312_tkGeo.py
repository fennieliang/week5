#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:33:46 2021

@author: fennieliang
"""

import tkinter as tk
 
# creating the tkinter window
window = tk.Tk() #instantiate an gui window
window.title('Python class window')#give the window a title
#window.geometry("300x300") #give the window a size


# set window width and height
mywidth = 300
myheight = 300

# get screen height and width
scrwdth = window.winfo_screenwidth()
scrhgt = window.winfo_screenheight()

# write formula for center screen
xLeft = int((scrwdth/2) - (mywidth/2))
yTop = int((scrhgt/2) - (myheight/2))

# centred the window in any size of the screen
window.geometry(str(mywidth) + "x" + str(myheight) + "+" + str(xLeft) + "+" + str(yTop))


'''
practice 

1. write a method called centre_math to a class named Tkinter_GUI 
that allows users to provide the width and height,
and position the window at the centre of the users' screens

2. do a call to check the class performs right

0304 allow the user to input width and height for the tkinter window
'''


# variable
my_text = "system updated !!!"
 
# function define for
# updating the my_label
# widget content
def counter():#change the name to see what happens
   
    # use global variable
    global my_text
     
    # configure
    my_label.config(text = my_text)
 
# create a button widget and attached  
# with counter function  
my_button = tk.Button(window,
                   text = "click to update",
                   command = counter)
 
# create a Label widget
my_label = tk.Label(window,
                 text = "update system")
 
# place the widgets
# in the gui window
my_label.pack()
my_button.pack()

# Start the GUI
window.mainloop()
