def solicitar_numero(mensaje):
    "Solicitar numero al usuario"
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválidad, ingresar un número entero")

num1 = solicitar_numero("Ingrsar el primero número: ")
num10= 10

if (num1 > num10):
    print("El número: ", num1 , " es mayor al número ", num10)
else:
    if (num10 > num1):
        print("El número: ", num1 , "es menor al número: ", num10)
    else:
        if (num1 == num10):
            print("El número: ", num1, " es igual número: ", num10)