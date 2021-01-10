veces=(int(input('Ingrese la cantidad de dias que debe tomar el medicamento: ')))
dia=(int(input('Ingrese la cantidad de veces que debe tomarlo: ' )))
numero_comprimidos=(int(input('Ingrese cantidad de comprimidos del envase: '))) 
resultado = (veces * dia / numero_comprimidos)
def calculo_dosis ():
	if resultado <=1:
		return "verdadero"
	else:
		return "falso"
print(calculo_dosis())
