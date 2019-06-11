from tkinter import *
import tkinter as tk
import subprocess as sub
from  tkinter.scrolledtext import *

WINDOW_SIZE = "700x500"

root = tk.Tk()

def display():
    text = Text(root)
    p = sub.Popen('/home/gp/PycharmProjects/eg/shellscript.sh', stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = p.communicate()
    print(output)
    text.pack()
    text.insert(END, output)
    text.place(relx=.1, rely=.15, height=400, width=500)

def getdata():
    f = open("tum2.txt")
    text = Text(root)
    text.insert(INSERT,f.read())
    text.pack()
    text.place(relx=.1,rely=.15,height=400, width=500)

def exit():
    root.quit()

#sh=ScrolledText(root,width=100,height=100).pack()

root.geometry(WINDOW_SIZE)
l1 = tk.Label(root, text="Tumour Data Analysis")
l1.pack()

b1 = Button(root, text="generate tree", command=display)
b1.pack()
b1.place(relx=.3, rely=.1, anchor="c")

b2 = Button(root, text="Data", command=getdata)
b2.pack()
b2.place(relx=.5, rely=.1, anchor="c")

b2 = Button(root, text="exit", command=exit)
b2.pack()
b2.place(relx=.7, rely=.1, anchor="c")

root.mainloop()
