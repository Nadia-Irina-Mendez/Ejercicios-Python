#Ejercicio 2: Escribir un programa que calcule la sumatoria desde 0 hasta m, donde m es
#un número introducido por el usuario desde el teclado.

total = 0
m=int(input("Ingrese la cant de numeros:"))
for i in range(0,m): # range(0,m) es lo mismo que tener (0,1,2,3,4....m)
	total=total+i
	print("Usando for",i)
print("Sumatoria :",total)



#while caso 2
m=int(input("Ingrese la cantidad de veces a procesar el bucle: "))
total=0
i=0
while i<m: # se pueden poner multiples condiciones para evaluar
	total=total+i
	print("Usando while",i)	
	i = i + 1  
print("Sumatoria :",total)
