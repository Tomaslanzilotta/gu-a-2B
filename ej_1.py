numeros_pares = 0
numero = int(input("Introduce un número entre el 1 y el 10 o escribe 0 para detener: "))

while numero != 0 and numero<=10: 
    if numero % 2 == 0:
        numero = int(input("Introduce un número entre el 1 y el 10 o escribe 0 para detener: "))
        numeros_pares += 1
    else:
        numero = int(input("Introduce un número entre el 1 y el 10 o escribe 0 para detener: "))
 
 
print("Conteo de números pares:", numeros_pares)