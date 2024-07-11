acumulador = 0
cantidad = 0

while cantidad !=5:
    numero = float(input("ingresar numero: "))
    cantidad+=1
    acumulador = acumulador + numero


print("la suma acumulada es: ",acumulador)
print("el promedio de los numeros ingresados es: ", acumulador/5)