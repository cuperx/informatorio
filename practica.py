"""
for i in range(100,1000):
	c = i//100
	d = (i//10)%10
	e = i%10
	if (c**3 + d**3 + e**3) == i:
		print("El resultado de la es correcto:", i)

print("---------------------------------------------")

for i in range(100,1000):
	a = str(i)
	
	for x in a:
		suma = int(x)**3
		if suma==i:
			print(i)
"""
"""
def config(**param):
	for x in param:
		print(x, ":", param[x])

config(fuente ="arial", tamaño= 12, color= "rojo")
"""
#a = [1, 2, 3]


#lista= ["sapo", "mosquito", "rata", "gato"]

#elemento=lista.pop(2)
#print(elemento)

#lista=[1, 2 , 3, 4, 4, 7, 6, 1, 2, 3, 5, 7, 6, 6, 6, 6]
#print(lista.count())
"""
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)
"""
"""DESAFÍO 4
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado.
Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6"""


fila = int(input("Ingrese cantidad de filas para el tablero: "))
columna = int(input("Ingrese cantidad de columnas para el tablero: "))
verde = " (VE) "
blanco = " )BA( "
for i in range(fila):
	for j in range (columna):
		if (i + j)%2 == 0: 
			print(verde, end="")
		else:
			print(blanco, end="")
	print("\n")	
