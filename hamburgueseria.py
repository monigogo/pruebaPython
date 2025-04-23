inventario = 100
print(f"El inventario contiene{inventario} hamburguesas")
while inventario > 0:
    if inventario <= 10:
        print("El inventarion esta casi vacio")
    num_hamburguesas = int(input("Cuantas hamburguesas quiere el cliente?"))
    if num_hamburguesas > inventario:
            print(f"No hay suficientes hamburguesas en stock. Solo hay {inventario} ")
    else:
            inventario -= num_hamburguesas
            print(f"El cliente ah pedido {num_hamburguesas} hamnburguesas el inventario ahora tiene {inventario} hamburguesas")