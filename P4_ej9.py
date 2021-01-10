# Ejercicio 9: Diseñar un programa que dado un carácter imprima en pantalla si es una
# letra, un dígito, un carácter especial u otro tipo de carácter.

# para esto hay que usar la tabla ASCII
# de 65 a 90 letras mayusculas de A - Z
# de 97 a 122 letras minusculas de a - z
# de 48 a 57 numeros
# todo lo demas son caracteres especiales

# hay que usar un if multiple y la funcion ord()

caracter=input("Ingrese un caracter x teclado: ")
x=ord(caracter)
if x >= 0 and x <= 47:
	print("es un caracter")
elif x >= 48 and x <= 57:
	print(" es un numero")
elif x >= 58 and x <= 64:
	print(" es un caracter")
elif x >= 65 and x <= 90:
	print("es una letra mayuscula")
elif x >= 91 and x <= 96:
	print(" es un caracter")
elif x >= 97 and x <= 122:
	print("es una letra minuscula")
elif x >= 123 and x <= 127:
	print(" es un caracter") 
