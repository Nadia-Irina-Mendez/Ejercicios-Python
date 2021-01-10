#a
def crea_lista(): 
	lista_a=[]
	legajo=1
	while legajo !=0:
		legajo=input("ingrese número de legajo o el búmero 0 para finalizar: ")
		nombre=str(input("ingrese su nombre y apellido por favor: "))
		dni=int(input("ingrese su DNI sin espacios ni puntos: "))
		email=str (input("ingrese su e-mail: "))
		materias=str(input("Ingrese la cantidad de materias que haya aprobado: "))
		datos=(nombre,legajo,dni,email,materias)
		lista_a.append(datos)
	print(lista)
print(crea_lista())

#b
def nueva_lista(lista): 
	lista_completa=[]
	lista_incompleta=[]
	for ii in lista: 
			if lista_completa == [legajo,nombre,dni,email,materias]:
				print("Los alumnos", lista_completa, "tienen todos sus datos cargados a la BBDD")
				print(lista_completa)
	else:
		print("Los alumnos",lista_vacia, "no han cargado todos sus datos correctamente")
		print(lista_vacia)
print(nueva_lista())
	
#c	

def todas_las_listas(lista, nueva_lista):
	cantidad_alumno=0
	for foo in lista: 
		print(crea_lista(cantidad_alumno))
		print(nueva_lista(cantidad_alumno))
		cantidad_alumno=cantidad_alumno+1 
	print(crea_lista())
	print(nueva_lista())

#d

def menu_equipos():
	punto=0
	while opcion!=3: 
		print("Ingrese 1 para imprimir la lista original: ")
		print("Ingrese 2 para imprimir la lista más reciente: ")
		print("Ingrese 3 para salir: ")		
		punto=int(input("ingrese opcion: "))
		if punto==1:
			print(nueva_lista()) 			
		elif punto==2:
			print(todas_las_listas())	
print(menu_equipos())
	
