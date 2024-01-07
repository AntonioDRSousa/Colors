import tkinter as tk
from tkinter import ttk
import time

def change():
    color()
    win.after(1,change)

def hex_rgb(x):
    symb = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return symb[x // 16]+symb[x %  16]

def getTuple():
    r = hex_rgb(int(SP_R.get()))
    g = hex_rgb(int(SP_G.get()))
    b = hex_rgb(int(SP_B.get()))
    return (r,g,b)

def getRGB():
    r = int(SP_R.get())
    g = int(SP_G.get())
    b = int(SP_B.get())
    return str((r,g,b))

def make_text(event):
    t = getTuple()
    s = getRGB()+" | "+"#"+t[0]+t[1]+t[2]
    txt.configure(state='normal')
    txt.delete(1.0,tk.END)
    txt.insert(1.0,s)
    txt.configure(state='disable')


def color():
    t = getTuple()
    s = "#"+t[0]+t[1]+t[2]
    c.configure(bg=s)

def putLabel():
    L_R.grid(row=1,column=0,columnspan=1,rowspan=1,sticky="news")
    L_G.grid(row=2,column=0,columnspan=1,rowspan=1,sticky="news")
    L_B.grid(row=3,column=0,columnspan=1,rowspan=1,sticky="news")

def putScale():
    S_R.grid(row=1,column=2,columnspan=1,rowspan=1,sticky="news")
    S_G.grid(row=2,column=2,columnspan=1,rowspan=1,sticky="news")
    S_B.grid(row=3,column=2,columnspan=1,rowspan=1,sticky="news")

def putSpin():
    SP_R.grid(row=1,column=1,columnspan=1,rowspan=1,sticky="news")
    SP_G.grid(row=2,column=1,columnspan=1,rowspan=1,sticky="news")
    SP_B.grid(row=3,column=1,columnspan=1,rowspan=1,sticky="news")
    
def putScreen():
    putLabel()
    putSpin()
    putScale()
    c.grid(row=0,column=0,columnspan=3,rowspan=1,sticky="news")
    B_Make.grid(row=4,column=0,columnspan=2,rowspan=1,sticky="news")
    txt.grid(row=4,column=2,columnspan=1,rowspan=1,sticky="news")


win = tk.Tk()
win.geometry('1000x600')
win.resizable(False,False)
win.title('Colors')

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='RGB')
tabControl.pack(expand = 1, fill ="both")

c = tk.Canvas(tab1)

f = ('Helvetica',10,'bold')

L_R = tk.Label(tab1,bg="#FF0000",font=f,text="Red : ")
L_G = tk.Label(tab1,bg="#00FF00",font=f,text="Green : ")
L_B = tk.Label(tab1,bg="#0000FF",font=f,text="Blue : ")

vr = tk.IntVar(value=0)
vg = tk.IntVar(value=0)
vb = tk.IntVar(value=0)

S_R = tk.Scale(tab1, variable=vr, from_=0, to=255, orient='horizontal')
S_G = tk.Scale(tab1, variable=vg, from_=0, to=255, orient='horizontal')
S_B = tk.Scale(tab1, variable=vb, from_=0, to=255, orient='horizontal')

SP_R = tk.Spinbox(tab1, justify = tk.CENTER, from_=0, to=255, state = 'readonly', textvariable=vr, wrap=False)
SP_G = tk.Spinbox(tab1, justify = tk.CENTER, from_=0, to=255, state = 'readonly', textvariable=vg, wrap=True)
SP_B = tk.Spinbox(tab1, justify = tk.CENTER, from_=0, to=255, state = 'readonly', textvariable=vb, wrap=True)

B_Make = ttk.Button(tab1,text='Make Text')

txt = tk.Text(tab1, height=0,bg='#00FFFF', borderwidth=0)
txt.configure(state='disable')

putScreen()

B_Make.bind('<Button-1>',make_text)

change()
win.mainloop()
