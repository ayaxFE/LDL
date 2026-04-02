#3. Modificar el programa anterior para que ahora solicite el ingreso de dos números
#enteros, y que luego informe si el primero es o no mayor que el segundo, usando
#el formato 'X es mayor que Y' (o ‘X no es mayor que Y’). Si ambos números fueran
#iguales, deberá informar 'X es igual a Y'. Por ejemplo, si se ingresan 23 y 42, se
#mostraría '42 es mayor que 23'.


def solicitar_numero(mensaje):
    "Solicitar numero al usuario"

    while True: 
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválidad, ingresar un número entero")

num1 = solicitar_numero("Ingresar el primero número: ")
num2 = solicitar_numero("Ingresar el segundo número: ")

if (num1 > num2):
    print(num1, "es mayor que", num2)
else:
    if (num2 > num1):
        print(num1, "es menor que", num2)
    else:
        if (num1 == num2):
            print(num1, "es igual a", num2)


