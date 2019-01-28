from tkinter import *

root = Tk()
root.geometry('300x200')
print('hello')
root.title('графика')


def button():
    lab.config(text=ent.get())
    print(ent.get())


but = Button(root, text='ок', command=button)
but.pack()
lab = Label(root, text='нажмите на кнопку')
lab.pack()
ent = Entry(root)
ent.pack()

root.mainloop()
