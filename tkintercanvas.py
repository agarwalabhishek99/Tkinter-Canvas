import tkinter
from tkinter import *

m = tkinter.Tk()

m.geometry("400x400")
m.title("Canvas")

c = Canvas(m, bg="red", height="300", width="300")
c.pack()

m.mainloop()

