#6.Solicitar el ingreso de un número entero e imprimir los números correlativos
#desde el ingresado hasta el doble del mismo. Por ejemplo: si se ingresa un 6, se
#deberá mostrar: 6, 7, 8, 9, 10, 11, 12.

numero = int(input("ingrese un numero:"))
doble = numero*2

while (numero <= doble):
    print (numero)
    numero = numero+1
