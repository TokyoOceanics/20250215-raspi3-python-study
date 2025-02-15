#!/usr/bin/env python3

import tkinter
root=tkinter.Tk()

root.title("image read and display")
ca=tkinter.Canvas(width=1000,height=800)
ca.pack()

ga=tkinter.PhotoImage(file="01190155.png")
ca.create_image(500,400,image=ga)
root.mainloop()

