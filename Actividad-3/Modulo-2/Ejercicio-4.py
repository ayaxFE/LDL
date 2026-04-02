#4 Escribir un programa que solicite el ingreso de un número entero y, si el número
#leído es par, imprima la leyenda 'El número es PAR'. En caso contrario, deberá
#mostrar el texto 'El número es IMPAR'.


# ingresamos un numero entero que se mostraria por pantalla
numero = int(input("Ingrese un número entero: "))

#evaluamos si nuestro numero entero es par o impar
# para eso le aplicamos resolucion modulo, si su resultado
# es igual a cero es par sino es impar

if numero % 2 == 0:
    #resul. igual a 0
    print("El número es PAR")
else:
    #resul. distinto de cero
    print("El número es IMPAR")

