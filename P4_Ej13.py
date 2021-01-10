#Ejercicio 13: Dado la duración (en segundos) de una llamada telefónica, calcular su
#costo, de la siguiente manera: El primer minuto $1,10, luego $0,25 cada fracción de 15
#segundos (un cuarto de minuto).

llamada=int(input("Ingrese duracion de la llamada en seg: "))
if llamada<=60:
	print("El costo de la llamada es $1,10 ")
else: 
	if llamada%15==0: # contemplo las llamadas con duracion igual a multiplo de 15 segundos
		costo=1.10+((int((llamada-60)/15)))*0.25
	else:
		costo=1.10+(int((llamada-60)/15)+1)*0.25		
	print("El costo de su llamada es",costo)
 
