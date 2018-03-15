import sys

import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as tkFileDialog

root=tkinter.Tk()
root.title("WordNote 1.2")
text=Text(root)
text.grid()
text.insert(END,"<WordNote 1.2>")
def saveas():

    global text

    t = text.get("1.0", "end-1c")

    savelocation=tkFileDialog.asksaveasfilename()

    file1=open(savelocation, "w+")

    file1.write(t)

    file1.close()
button=ttk.Button(root, text="Save", command=saveas) 
button.grid()
def helvetica():
    global text
    text.config(font="Helvetica")
    
def courier():
    global text
    text.config(font="Courier")
    
def calibri():
    global text
    text.config(font="Calibri")

def system():
    global text
    text.config(font="System")

def corbel():
    global text
    text.config(font="Corbel")

def elephant():
    global text
    text.config(font="Elephant")

def ar():
    global text
    text.config(font="Arial")

                
font=ttk.Menubutton(root, text="Fonts") 
font.grid() 
font.menu=Menu(font, tearoff=0)
font["menu"]=font.menu
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=courier)
font.menu.add_checkbutton(label="Elephant", variable='elephant', 
command=elephant)
font.menu.add_checkbutton(label="Helvetica", variable="helvetica",
command=helvetica)
font.menu.add_checkbutton(label="Calibri", variable="calibri",
command=calibri)
font.menu.add_checkbutton(label="System", variable="system",
command=system)
font.menu.add_checkbutton(label="Corbel", variable='corbel',
command=corbel)
font.menu.add_checkbutton(label="Arial", variable='arial',
command=ar)
root.mainloop()
