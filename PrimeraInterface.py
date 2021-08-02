from tkinter import *

raiz=Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(1,1)
raiz.iconbitmap("favicon.ico")
raiz.geometry("1000x450")

raiz.mainloop()
miFrame=Frame(raiz)
miFrame.pack()
miImagen=PhotoImage(file="ahegao.gif")
Label(miFrame,image=miImagen).place(x=0,y=0)

raiz.mainloop()