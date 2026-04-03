#10.Escribir un programa que solicite el ingreso de 8 números enteros que se
#encuentren entre -10 y 10 e imprima la sumatoria de los valores negativos, la
#cantidad de valores iguales a cero y el promedio de los valores positivos. Se
#deberá pedir el reingreso de un número si éste estuviera fuera del rango dado.

lista_numeros = []
sumatoria_negativos = 0

for x in range(8):
    numero = int(input("Ingrese un número entre -10 y 10: "))
    while numero not in range(-10, 11):
        numero = int(input("El número no se encuentra entre -10 y 10. Ingrese otro: "))
    lista_numeros.append(numero)
print(f"Lista de números: {lista_numeros}")

print("La cantidad de ceros ingresados es de: ", lista_numeros.count(0))

for x in lista_numeros:
    if x < 0:
        sumatoria_negativos += x

print(f"Sumatoria de números negativos: {sumatoria_negativos}")

valores_positivos = [x for x in lista_numeros if x > 0]
if valores_positivos:
    promedio = sum(valores_positivos) / len(valores_positivos)
    print(f"Promedio de positivos: {promedio}")
else:
    print("No se encontraron números positivos.")
