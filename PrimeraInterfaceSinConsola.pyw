from tkinter import *

raiz=Tk()
raiz.title("Ventana de pruebas")
#raiz.resizable(1,1)
raiz.iconbitmap("favicon.ico")
#raiz.geometry("650x450")
raiz.config(bg="cyan")
raiz.config(bd=1)
raiz.config(relief="groove")
raiz.config(cursor="hand2")

miFrame=Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="1000",height="1000")
miFrame.config(bd=1)
miFrame.config(relief="sunken")
miFrame.config(cursor="pirate")

miImagen=PhotoImage(file="ahegao.gif")
Label(miFrame, text="QUIERO CULIAR",fg="red",font=("Comic sans MS",18)).place(x=100,y=200)
Label(miFrame,image=miImagen).place(x=0,y=0)













raiz.mainloop()
