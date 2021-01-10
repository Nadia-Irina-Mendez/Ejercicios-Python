#Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que comprar (son de 60x60 cm)
value1 = int(input("ingresa el largo del terreno: "))
value2 = int(input("ingresa el ancho del terreno: ")) 
metro_cuadrado = value1*value2
panes = metro_cuadrado/0.36
print ("se necesitarán ", int(panes), "panes de pasto para su terreno")

#Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una clave con esos datos (su clave seria sus iniciales seguido de un guión bajo y de su año de nacimiento) y mostrarla.
logeo = str(input("ingrese su nombre: "))
logeo_apellido = str(input("ingrese su apellido: "))
date = str(input("ingrese su día y mes de nacimiento(ejemplo: 20 de marzo): "))
year = str(input("ingrese el año de su nacimiento (ejemplo: 1990): "))
print ("Su contraseña es: ",logeo[0],logeo_apellido[0],"_",year)
print ("la contraseña se escribirá sin espacios, gracias")
