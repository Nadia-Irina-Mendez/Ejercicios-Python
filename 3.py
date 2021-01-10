cateto_op=int(input('ingrese el primer lado del triángulo: ') )
cateto_ady=int(input('Ingrese el segundo lado del triángulo: ') )
hipot=int(input('Ingrese el tercer lado del triángulo: ') )
triangulo= cateto_op+cateto_ady+hipot
if triangulo >=3:
	print("se ha formado un triángulo")
else:
	print ("Eso no es un triángulo")
