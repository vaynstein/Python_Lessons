from tkinter import *
root=Tk()
root.geometry('300x200')
print('hello')
root.title('графика')

def button():
   ent.get()


but=Button(root,text='ок', command= button)
but.pack()
Lab=Label(root, text='нажмите на кнопку')
Lab.pack()
ent=Entry(root)
ent.pack()
print(but)
#but.pack(side='left')
root.mainloop()
