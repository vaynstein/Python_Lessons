from tkinter import *
from random import randint

X, Y = 800, 600
R = 20

root = Tk()
root.geometry('{}x{}'.format(X,Y))
label = Canvas(root, width=X,height=Y, bg='black')

img = PhotoImage(width=X,height=Y)

for i in range(10000):
    img.put('red', (randint(0,X), randint(0,Y)))

label.create_image(0, 0, anchor=NW, image=img)

for i in range(100):
    x = randint(0,X)
    y = randint(0,Y)
    r = randint(3, R)
    label.create_oval(x-r, y-r, x+r, y+r, fill='yellow')

label.pack()

root.mainloop()