#ejercicio 7: Escriba un programa que, leyendo del teclado los valores de sexo y altura, determine si es una persona petisa, normal o alta.

def funcion(sexo,altura):
	if sexo=="femenino":
		if altura <= 145:
			print("petisa")
		elif altura >=145 and altura <=170:
			print("normal")
		elif altura >= 170:
			print("alta")
	elif sexo=="masculino":
		if altura <=160:
			print("petiso")
		elif altura >=160 and altura <=190:
			print("normal")
		elif altura >=190:
			print("alto")
	else:
		print("opcion no disponible")
   
sexo=input("ingrese el genero de una persona (masculino/femenino): ")
altura=int(input("ingrese la altura de una persona en cm: "))

# llamado a la funcion
funcion(sexo,altura)

