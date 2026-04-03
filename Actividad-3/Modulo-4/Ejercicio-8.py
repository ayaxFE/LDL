#8.Escribir un programa que solicite ingresar una cantidad de números enteros a
#procesar. Luego, permitir al usuario ir ingresando uno a uno la cantidad pedida
#de números. Una vez finalizado el ingreso, se deberá mostrar la suma total de los
#números ingresados.

total_num = int(input("Ingrese la cantidad de numeros a procesar: "))
numeros = 0
sum_total = 0

while numeros < total_num:
    numeros = int(input("Ingrese un numero: "))
    sum_total += numeros
    
print("La suma de todos los numeros es: ", sum_total)    