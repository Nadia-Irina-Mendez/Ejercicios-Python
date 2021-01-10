#Ejercicio 6: Escriba un programa que lea nombres de personas hasta que se ingrese el
#nombre “zzz”. Debe imprimir la cantidad de nombres que comienzan con “A”.

cant=0
nombre=input("Ingrese el nombre:")
while nombre!="zzz":
	if nombre[0]=="A":
		cant=cant+1
	nombre=input("Ingrese el nombre:")

print("La cantidad de nombres que comienzan con A ingresados es",cant)

 
