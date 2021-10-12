#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:41:01 2021

@author: fennieliang
"""
import tkinter as tk
from tkinter import *
from tkinter import filedialog  
from lesson_03_class import Text_process as T



def word_fre_label(fict):
    dic_text = ""
    for i in fict :
        dic_text = dic_text +  i +" : "+ str(fict[i]) + "\n"
    return dic_text


def process():
    global content_label, dict_label, a
    content = textarea.get('0.0','end')
    word_dic = T.bag_word(T.doc_split_word(content))
    del word_dic['']
    print(word_dic)
    dict_label['text'] =  word_fre_label(word_dic)
    path.grid(column = 0, row = 2  , sticky=tk.W)
    read_file_bt.grid(column = 0, row = 2  , sticky=tk.E)
    process_bt.grid(column = 0, row = 3  , sticky=tk.E)
 
    return 
    

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="/Users/fennieliang/Documnets/GitHub/python/lesson03", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    path.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    textarea.insert(END, data)
    tf.close()

# Create a GUI app
wd = tk.Tk()

# Give a title to your app
wd.title("My Python Class")
wd.geometry("570x600") 

textarea = tk.Text(wd)
textarea.grid(column = 0, row = 0, sticky=tk.W)

dict_label = tk.Label(wd, justify = 'left' )
dict_label.grid(column = 0, row = 1, sticky=tk.W+tk.N)


path = tk.Entry(wd)
path.grid(column = 0, row = 2, sticky=tk.W)


read_file_bt = tk.Button(wd, height=1, width=10, text="Read File", command=openFile)
read_file_bt.grid(column = 0, row = 2, sticky=tk.E)


process_bt = tk.Button(wd, text = "Process", command=process)
process_bt.grid(column = 0, row = 3, sticky=tk.E)
 

wd.mainloop()