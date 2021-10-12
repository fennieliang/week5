from tkinter import *
import tkinter as tk

from tkinter import filedialog  


def copy_text():
    content = textarea.get('0.0','end')
    tk.Label(wd, text = content, justify = 'left').place(x = 0, y = 101)

    print(content)
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
wd.geometry("570x500") 

textarea = tk.Text(wd)
textarea.place(x = 0, y = 0, width=570, height=100)

path = tk.Entry(wd)
path.pack(side="left", expand="yes", fill="x")



tk.Button(
    wd, height=1, width=10,
    text="Read File", 
    command=openFile
    ).pack(side="right",  expand="yes", fill="x")


tk.Button(wd, text = "copy", command=copy_text).place(x = 500, y = 450, width=70)


wd.mainloop()