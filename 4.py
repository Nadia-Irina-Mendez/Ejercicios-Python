pulsacion=int(input('ingrese la cantidad de pulsaciones por minuto: ') )
if pulsacion <210:
	print ("sus pulsaciones son demasiado bajas")
elif pulsacion >220:
	print("sus pulsaciones son aceleradas")
elif pulsacion >=210 and pulsacion <=220: 
	print("Sus latidos son normales")

