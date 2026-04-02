#7. Solicitar el ingreso de un número entero. Si el número ingresado es impar, se
#deberán imprimir los números correlativos desde el ingresado hasta el doble del
#mismo. Si el número ingresado es par, se deberán mostrar los números pares
#desde el ingresado hasta el doble del ingresado. Por ejemplo: si se ingresa un 8,
#se mostrará 8, 10, 12, 14, 16. Si se ingresa un 5, se mostrarán 5, 6, 7, 8, 9, 10.

def es_par(x):
    return x % 2 == 0

def pedir_numero():
    numero = int(input("Ingrese número entero: "))
    try:
        numero = int(numero)
    except ValueError:
        print("No es un número entero")
    return numero

num = pedir_numero()

if not es_par(num):
    print(num)
    for num in range(num, (2 * num)):
        print(num + 1)
else:
    for num in range(num, (2 * num) + 1):
        if es_par(num):
            print(num)
