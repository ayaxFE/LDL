#4 Escribir un programa que solicite el ingreso de un número entero y, si el número
#leído es par, imprima la leyenda 'El número es PAR'. En caso contrario, deberá
#mostrar el texto 'El número es IMPAR'.


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

