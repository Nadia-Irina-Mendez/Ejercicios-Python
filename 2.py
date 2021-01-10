meses=input('Ingrese el número del mes que desee: ' )
def cuantos_dias(mes):
	if mes.lower() in ("1","3","5","7","9","11"): 
		return "31 días"
	elif mes.lower() == "2":
		return "28 días"
	else:
		return "30 días"
print(cuantos_dias(meses))
