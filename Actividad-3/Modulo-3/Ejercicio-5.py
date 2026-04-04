#5. Solicitar al usuario que ingrese el día de la semana y la cantidad de artículos
#comprados por un cliente en un comercio. Finalmente, imprimir “accede al
#descuento” si el día es lunes y el cliente compró más de 3 artículos. En caso
#contrario, no imprimir nada.

dia = str(input("ingrese un dia:").strip().lower())
cantidadArticulos = int(input("ingrese la cantidad de articulos:"))

if (dia=="lunes") and (cantidadArticulos>3):
    print ("Accede al descuento")
