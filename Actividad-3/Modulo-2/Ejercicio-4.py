#4 Escribir un programa que solicite el ingreso de un número entero y, si el número
#leído es par, imprima la leyenda 'El número es PAR'. En caso contrario, deberá
#mostrar el texto 'El número es IMPAR'.



numero = int(input("Ingrese un número entero: "))

try:
    numero = int(numero)
except ValueError:
    print("El valor ingresado no es un número entero válido.")


if numero % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")

print ("vamos los pibes")