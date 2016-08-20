from functools import partial
import Tkinter
root=Tkinter.Tk()
mybutton=partial(Tkinter.Button,root,fg='white',bg='black')
b1=mybutton(text='Button 1')
b2=mybutton(text='Button 2')
qb=mybutton(text='QUIT',bg='red',command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X,expand=True)
root.title('PFAs!')
root.mainloop() 