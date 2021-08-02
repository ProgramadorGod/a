from tkinter import *
raiz = Tk()
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre=StringVar()

cuadroTexto1=Entry(miFrame,textvariable=minombre)
cuadroTexto1.grid(row=0,column=1,padx=10,pady=10)
cuadroTexto1.config(fg="red",justify="left")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(show="X")

cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=2,column=1,padx=10,pady=10)

cuadroTexto3=Entry(miFrame)
cuadroTexto3.grid(row=3,column=1,padx=10,pady=10)

TextoComentario=Text(miFrame,width=16,height=5)
TextoComentario.grid(row=4,column=1,padx=10,pady=10)

scrollVert=Scrollbar(miFrame,command=TextoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew")
TextoComentario.config(yscrollcommand=scrollVert.set)


nombreLabel1=Label(miFrame, text="Nombres:")
nombreLabel1.grid(row=0,column=0,padx=10,pady=10, sticky="e")

nombreLabel2=Label(miFrame, text="Apellidos:")
nombreLabel2.grid(row=2,column=0, sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Password")
passLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

nombreLabel3=Label(miFrame, text="Dirección:")
nombreLabel3.grid(row=3,column=0, sticky="e",padx=10,pady=10)

comentariosLable=Label(miFrame,text="Comentario: ")
comentariosLable.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoBoton():
	minombre.set("luis")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()



raiz.mainloop()