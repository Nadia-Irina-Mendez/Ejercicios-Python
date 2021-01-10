#Ejercicio 4: Escribir un programa que lea letras del teclado indefinidamente hasta que el
#usuario ingrese “fin” e imprima el código ASCII de las mismas.

letra=input("Ingrese una letra:")
while letra != "fin":
	print(ord(letra))
	letra=input("Ingrese una letra:")


#no tengo posibilidad de usar FOR
 
