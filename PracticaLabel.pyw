from tkinter import *
root=Tk()
miFrame=Frame(root,width=1000,height=1000)
miFrame.pack()
miImagen=PhotoImage(file="ahegao.gif")
Label(miFrame,image=miImagen).place(x=0,y=0)
root.mainloop()