#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:43:31 2021

@author: fennieliang

a tkinter window for text input
"""
import tkinter as tk

window = tk.Tk()

def getTextInput():
    
    #get the first character to the end of the input
    result=textExample.get("1.0","end")    
    print(result)
    

textExample=tk.Text(window)# width=100, height=10
textExample.config(font="ariel",bg="#E1DDE6",fg="red")
textExample.pack(side="top")
'''
btHello=tk.Button(window, height=1, width=10, text="Hello",font=("helvetica",20, "underline italic"))

btHello.pack(side="left",fill="y")
'''
btnRead=tk.Button(window, text="Process",  fg="green",
                    command=getTextInput)
#add action to get a user's input


btnRead.pack(side="bottom", expand="yes", fill="x")
window.title("The Python Class")
window.mainloop()


