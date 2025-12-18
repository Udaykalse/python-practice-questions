from tkinter import *

root=Tk()
canvas=Canvas(root,width=400,height=300)
canvas.pack()

ball=canvas.create_oval(10,10,40,40, fill='blue')


def move():

    canvas.move(ball,5,0)
    root.after(100,move)


move()

root.mainloop()