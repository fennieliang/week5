#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 16:13:16 2021

@author: fennieliang
"""
import tkinter as tk
#from tkinter import *
from tkinter import filedialog

def openFile():
    tf = filedialog.askopenfilename(
        #change to your own directory below to have a correct path
        initialdir="/Users/fennieliang/Documnets/GitHub/python/lesson03", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    path.insert(tk.END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(tk.END, data)
    tf.close()

ws = tk.Tk()
ws.title("My Python Class")
ws.geometry("500x500")
ws['bg']='#5CF9F2'

txtarea = tk.Text(ws, width=100, height=20)
txtarea.pack(pady=20)

path = tk.Entry(ws)
path.pack(side="left", expand="yes", fill="x")



tk.Button(
    ws, height=1, width=10,
    text="Open File", 
    command=openFile
    ).pack(side="right",  expand="yes", fill="x")


ws.mainloop()