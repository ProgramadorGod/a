from tkinter import *


raiz=Tk()

miFrame2=Frame(raiz,width=1000,height=1000)
miFrame2.pack()
miImagen=PhotoImage(file="ahegao.gif")
Label(miFrame2,image=miImagen).place(x=0,y=0)
miFrame=Frame(raiz,width=1000,height=1000)
miFrame.pack()
miFrame.place(x=400,y=0)

operacion=""
resultado=0
operacionmomentanea=""
limitante=0
yameti=0
primeravez = 1
resultado_resta = 0
valor1=0
valor2=0
permiso_igual=1
#----------------Pantalla-----------------

botonn1=StringVar()
botonn2=StringVar()
botonn3=StringVar()
botonn4=StringVar()
botonn5=StringVar()
botonn6=StringVar()
botonn7=StringVar()
botonn8=StringVar()
botonn9=StringVar()
botonn0=StringVar()

NumeroPantalla=StringVar()

miFrame.config(bg="red")
miFrame.config(bd=10)
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")
pantalla=Entry(miFrame,textvariable=(NumeroPantalla))
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(bg="black",fg="#03f943", justify="right")


#----Funciones-----
def NumeroPulsado(num):
	global operacionmomentanea
	global operacion
	global limitante
	if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6" or num == "7" or num == "8" or num == "9" or num == "0":
		limitante = 0
	if operacion == "suma":
		NumeroPantalla.set(num)
		operacion=""
		operacionmomentanea="suma"
	elif operacion == "resta":
		NumeroPantalla.set(num)
		operacion=""
		operacionmomentanea="resta"
	elif operacion == "multiplicacion":
		NumeroPantalla.set(num)
		operacionmomentanea="multiplicacion"
		operacion=""
	elif operacion == "division":
		NumeroPantalla.set(num)
		operacion=""
		operacionmomentanea="division"
	elif operacion == "":
		NumeroPantalla.set(NumeroPantalla.get() + num)




#-------------------------FILA 1--------------------

boton7=Button(miFrame,text="7", width=3,command=lambda:NumeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8", width=3,command=lambda:NumeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9", width=3,command=lambda:NumeroPulsado("9"))
boton9.grid(row=2,column=3)
boton_div=Button(miFrame,text="/", width=3,command=lambda:division(NumeroPantalla.get()))
boton_div.grid(row=2,column=4)

#---------------------FILA 2 ----------------------

boton4=Button(miFrame,text="4", width=3,command=lambda:NumeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5", width=3,command=lambda:NumeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6", width=3,command=lambda:NumeroPulsado("6"))
boton6.grid(row=3,column=3)
boton_multiplicar=Button(miFrame,text="x", width=3,command=lambda:multiplicacion(NumeroPantalla.get()))
boton_multiplicar.grid(row=3,column=4)

#------------------------FILA 3---------------
boton1=Button(miFrame,text="1", width=3,command=lambda:NumeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2", width=3,command=lambda:NumeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3", width=3,command=lambda:NumeroPulsado("3"))
boton3.grid(row=4,column=3)
botonResta=Button(miFrame,text="-", width=3,command=lambda:resta(NumeroPantalla.get()))
botonResta.grid(row=4,column=4)

#---------------------FILA 4--------------
boton0=Button(miFrame,text="0", width=3,command=lambda:NumeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",", width=3,command=lambda:NumeroPulsado(","))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=", width=3,command=lambda:El_Igual(NumeroPantalla.get()))
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame,text="+", width=3,command=lambda:suma(NumeroPantalla.get()))
botonSuma.grid(row=5,column=4)




#----------------------------FUNCION SUMA-----------------------------------------
def suma(num):
	global operacion
	global operacionmomentanea
	operacionmomentanea = "suma"
	operacion="suma"
	global resultado
	global limitante
	if limitante == 0:
	 	resultado+=int(num)
	 	limitante = 1
	NumeroPantalla.set(resultado)

#--------------------------FUNCION RESTA--------------------------------
def resta(num):
	global operacion
	global valor1
	global valor2
	global operacionmomentanea
	global primeravez
	global yameti
	global resultado_resta
	operacionmomentanea = "resta"
	operacion="resta"
	global resultado
	global limitante
	if limitante == 0:
		if primeravez == 1:
			resultado =resultado+int(num)
			valor1=resultado
			NumeroPantalla.set(resultado)
		elif primeravez == 0:
			valor2=valor2+int(num)
			resultado=valor1-valor2
			NumeroPantalla.set(resultado)
		limitante+=1
	else:
		if primeravez == 1:
			NumeroPantalla.set(valor1)
		else:
			NumeroPantalla.set(resultado)
	primeravez = 0
	yameti = 1
#-------------------------------FUNCION MULTIPLICACION----------------------

def multiplicacion(num):
	global operacion
	global operacionmomentanea
	operacionmomentanea = "multiplicacion"
	operacion="multiplicacion"
	global resultado
	global limitante
	if limitante == 0:
	 	resultado*=int(num)
	 	limitante = 1
	NumeroPantalla.set(resultado)

#-------------------------------FUNCION DIVISION----------------------------

def division(num):
	global operacion
	global operacionmomentanea
	operacionmomentanea = "division"
	operacion="division"
	global resultado
	global limitante
	if limitante == 0:
	 	resultado/=int(num)
	 	limitante = 1
	NumeroPantalla.set(resultado)

#----------Funcion El_Igual---------------------------------------
def El_Igual(num):
	global resultado

	if operacionmomentanea == "suma":	
		NumeroPantalla.set(resultado+int(NumeroPantalla.get()))
		resultado = 0
	elif operacionmomentanea=="resta":
		Igual_resta(num)
def Igual_resta(num):
	global resultado
	global valor1
	global valor2
	global permiso_igual
	global limitante

	if operacionmomentanea == "resta":
		resultado = valor1-int(num)
		if limitante ==0:
			if primeravez == 1:
				NumeroPantalla.set(resultado)
			else:
				NumeroPantalla.set(resultado)
			limitante=1
	




#------------------Operacion momentanea---------



raiz.mainloop()