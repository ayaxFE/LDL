#3. Modificar el programa anterior para que ahora solicite el ingreso de dos números
#enteros, y que luego informe si el primero es o no mayor que el segundo, usando
#el formato 'X es mayor que Y' (o ‘X no es mayor que Y’). Si ambos números fueran
#iguales, deberá informar 'X es igual a Y'. Por ejemplo, si se ingresan 23 y 42, se
#mostraría '42 es mayor que 23'.

#evitamos incongruencia de tipo de datos
#si el usuario ingresa un String genera error de tipo
#si o si se tendra que ingresar un Int
#equivalente al Try Catch (Java POO)
def solicitar_numero(mensaje):
    "Solicitar numero al usuario"
    #bucle infinito hasta que se ingrese un Int
    while True: 
        try:
            #evualua, si es correcto cierra bucle
            return int(input(mensaje))
        except ValueError:
            #si el error ocurre mostrar
            print("Entrada inválidad, ingresar un número entero")

#pedir numeros al usuario
num1 = solicitar_numero("Ingresar el primer número: ")
num2 = solicitar_numero("Ingresar el segundo número: ")

#evaluamos mayor y menor
if (num1 > num2):
    print(num1, "es mayor que", num2)
elif (num2 > num1):
        print(num2, "es mayor que", num1)
else:
        if (num1 == num2):
            print(num1, "es igual a", num2)


