number1 = int(input("Inserta el numero 1: "))

number2 = int(input("Inserta el numero 1: "))

def sum(number1, number2):
    result =number1 + number2
    print(result)
def resta(number1, number2):
    result = number1 - number2
    print(result)
def div(number1, number2):
    if(number2!= 0):
        resul =number1/number2
        print(resul)
    else:
        print("ingresar un numero mayor a 0")
def mult(number1, number2):
    result= number1*number2
    print(result)
sum(number1,number2)
resta(number1,number2)
div(number1,number2)
mult(number1,number2)