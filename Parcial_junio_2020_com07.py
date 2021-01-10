#1- Programe modularizando una solución que permita manejar repuestos:

#a) Realice una función que cree una lista con información de repuestos. De cada producto se solicita:
# código, descripción, precio de costo, precio de venta, ubicación y tipo de repuesto (pudiendo ser N nuevo o U usado).
# La carga de productos finaliza cuando se ingresa el repuesto cuyo código sea igual a 999.

#b) Realice una función que utilizando la lista de productos creada en a) agregue a una nueva lista 
#la información completa de los artículos nuevos y a otra lista la información completa de los artículos usados.

#c) Realice una función que retorne el costo promedio de los artículos usados.

#d) Defina en una nueva función un menú que permita llamar a las funciones definidas en los puntos a, b y c.

#Nota: debe realizar todas las funciones y sus invocaciones con los parámetros que correspondan.


# a)  
def carga_datos(): # 99.99 % de los casos va sin parametros
	lista=[]
	codigo=int(input("ingrese codigo o 999 para finalizar: "))
	while codigo!=999:
		descri=input("ingrese descripcion: ")
		precos=int(input("ingrese precio de costo: "))
		preven=int(input("ingrese precio de venta: "))
		ubicacion=input("Ingrese ubicacion: ")
		tipo=input("Ingrese tipo: ")
		data=(codigo,descri,precos,preven,ubicacion,tipo)
		lista.append(data)
		codigo=int(input("ingrese codigo o 999 para finalizar: "))
	print(lista)
	return lista

# b) # separa en 2 listas los repuestos
def funcion_b(lista): 
	rep_nuevo=[]
	rep_usado=[]
	for x in lista: # 99.99 % de los casos se usa un for para recorrer una lista
		if x[5]=="N":
			rep_nuevo.append(x)
		if x[5]=="U":
			rep_usado.append(x)	
	print(rep_nuevo)
	print(rep_usado)	
	return rep_nuevo,rep_usado
            
# c) hay 2 opciones: usar la lista original o usar la lista de usados creada en b)
# calcula el promedio de articulos usados
def funcion_c(lista):
	promedio=0
	cant=0
	total=0 
	for x in lista: # recorro la lista original
		if x[5]=="U": # pregunto por la condicion de usado 
			total=total+x[2]
			cant=cant+1 
	promedio=total/cant	
	print("El precio de costo promedio es: ",promedio)			
	return promedio  
   
# d) # crea el menu
def menu(lista):
	opcion=0
	while opcion!=3: 
		print("Ingrese 1 para crear las 2 listas(punto b): ")
		print("Ingrese 2 para calcular el costo promedio(punto c) : ")
		print("Ingrese 3 para salir: ")		
		opcion=int(input("ingrese opcion: "))
		if opcion==1:
			funcion_b(milista) 			
		elif opcion==2:
			funcion_c(milista) 		


milista=carga_datos()
menu(milista)





