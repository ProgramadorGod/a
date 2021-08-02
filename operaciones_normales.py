f=1
while f == 1:	
	def suma():
		resultado=int(valor1 + valor2)
		print(resultado)
	def resta():
		resultado=valor1 - valor2
		print(resultado)
	def multiplicacion():
		resultado=int(valor1*valor2)
		print(resultado)
	def division():
		resultado=valor1 / valor2
		print(int(resultado))

	valor1=int(input("numero"))
	a=input("que quieres hacer:")
	valor2=int(input("numero"))
	if a== "suma":
		suma()

