#9.Modificar el programa anterior para que, si se ingresa un número negativo, no se
#sume, pero continúe con el proceso. Finalmente, mostrar por separado la suma
#de los números positivos pares e impares ingresados.

total_num = int(input("Ingrese la cantidad de numeros a procesar: "))
contador_num = 0
sum_total_pares = 0
sum_total_impares = 0
sum_total = 0

while contador_num < total_num:
    numeros = int(input("Ingrese un numero: "))
    if numeros >= 0:
        sum_total += numeros    
        if numeros %2 == 0:
            sum_total_pares += numeros
        else:
            sum_total_impares += numeros    
    else:
        print("El numero ingresado no se sumará")    
    contador_num += 1

print("La suma de todos los numeros pares es: ", sum_total_pares) 
print("La suma de todos los numeros impares es: ", sum_total_impares)   