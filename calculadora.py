print("------------------------------------------ ")
print(" BIENVENIDO A LA CALCULADORA INTERARCTIVA")
print("------------------------------------------")

menu = None
while menu is None or 1:
	if menu == None:
		menu = int(input("\n¿Desea ver el munú? \n1-Si \n2-No "))
	elif menu == 1:
		for i in ["Menu:","1-Sumar", "2-Restar", "3-Multiplicar", "4-Dividir", "5-Resto", "6-Salir"]:
			print(i)
		opcion = int(input("Ingrese el número a la opción "))
	
	# Sumar

		while opcion == 1:
			print("SUMAR")
			x= int(input("ingrese el primer número: "))
			y= int(input("ingrese el segundo número: "))
			print("El resultado de la suma es : ", x + y)
			repetir=int(input("\n ¿Desea repetir la operación? \n 1-Si \n 2-No"))
			if repetir == 1:
				opcion=1
			else: 
				opcion=None
				menu=1

	# Restar

		while opcion == 2:
			print("RESTAR")
			x= int(input("ingrese el primer número: "))
			y= int(input("ingrese el segundo número: "))
			print("El resultado de la resta es : ", x - y)
			repetir=int(input("\n ¿Desea repetir la operación? \n 1-Si \n 2-No"))
			if repetir == 1:
				opcion=2
			else: 
				opcion=None
				menu=1

	# Multiplicar

		while opcion == 3:
			print("MULTIPLICAR")
			x= int(input("ingrese el primer número: "))
			y= int(input("ingrese el segundo número: "))
			suma= 0
			while y != 0:
				suma= suma+x
				y=y-1
			print("El resultado de la multiplicación es : ", suma)
			repetir=int(input("\n ¿Desea repetir la operación? \n 1-Si \n 2-No"))
			if repetir == 1:
				opcion=3
			else: 
				opcion=None
				menu=1

	# Dividir

		while opcion == 4:
			print("DIVIDIR")
			x= int(input("ingrese el primer número: "))
			y= int(input("ingrese el segundo número: "))
			xrest = x - y
			contador=0
			while xrest >=  0:
				contador= contador + 1
				xrest = xrest - y
			print("El resultado de la multiplicación es : ", contador)
			repetir=int(input("\n ¿Desea repetir la operación? \n 1-Si \n 2-No"))
			if repetir == 1:
				opcion=4
			else: 
				opcion=None
				menu=1

		while opcion == 5:
			print("RESTO")
			x= int(input("ingrese el primer número: "))
			y= int(input("ingrese el segundo número: "))
			xrest = x - y
			while xrest >  0:
				xrest= xrest - y	
			print("El resto de la divivición es : ", xrest)
			repetir=int(input("\n ¿Desea repetir la operación? \n 1-Si \n 2-No"))
			if repetir == 1:
				opcion=5
			else: 
				opcion=None
				menu=1

	# Salir

		while opcion == 6:
			salir= int(input("\n¿Desea realmente salir del programa? \n 1-Si \n 2-No"))
			if salir ==1:
				opcion=None
				menu=3
			else:
				opcion=None
				menu=1
	else:
		break
print("Gracias por usar la calculadora interactiva")			

