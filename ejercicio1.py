"¿Cual es tu nombre?"#Declarar variable
nombre = input ("¿Cual es tu nombre?")
#edad = int(input("¿Cual es tu edad?"))
#print(f"hola {nombre}! Tienes {edad} años")

#def saludar(nombre):
 #   print(f"¡Hola,{nombre}! bienvenidos")
#saludar(nombre)

#for recorrer in range(1,10):
    #print(recorrer)
edad = int (input("Introduce tu edad"))
def esMayorEdad(edad):
    if edad >= 18:
          return "Eres mayor de edad"
    else:
        return "Eres menor de edad"
print(esMayorEdad(edad))
