def solicitar_numero(mensaje):
    "Solicitar numero al usuario"
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválidad, ingresar un número entero.")

# Pedir numeros al usuario
num1 = solicitar_numero("Ingresa el primero número: ")
num2 = solicitar_numero("Ingresa el segundo número: ")

print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Multiplicación: ", num1 * num2)

# Validar división por cero
if num2 !=0:
    print("Cociente: ", num1 // num2)
    print("Resto: ", num1 % num2)
else:
    print("No se puede dividir por cero")