from tkinter import *
raiz = Tk()

varoOpcion=IntVar()

def imprimir():
	#print(varoOpcion.get())
	if varoOpcion.get() == 1:
		etiqueta.config(text="Has elegido masculino")
	else:
		etiqueta.config(text="Has elegido femenino")
Label(raiz, text="Sexo").pack()

Radiobutton(raiz,text="masculino",variable=varoOpcion,value=1,command=imprimir).pack()
Radiobutton(raiz,text="femenino",variable=varoOpcion,value=2,command=imprimir).pack()

etiqueta=Label(raiz)
etiqueta.pack()


























raiz.mainloop()