while True:
    try:

        var = int(input("Ingrese un numero: "))
        var_2 = int(input("Ingrese un segundo numero: "))
        break

    except ValueError:
        print("Los valores ingresados no son correctos.")
    finally:
        print("Intentelo otra vez.")

try:
    opcion = int(input("Eliga la operacion que quiera realizar \n1-->Sumar\n2-->Restar\n3-->Multiplicar\n COLOQUE EL NUMERO DE LA OPERACION QUE QUIERA REALIZAR: "))
except ValueError:
    print("El valor ingresado no coincide con las opciones.")


try:
    if opcion == 1:
        print("La suma de los dos nuemro es: ", var + var_2)
    elif opcion == 2:
        print("La resta de los dos numeros es: ", var- var_2)
    elif opcion == 3:
        print("La Multiplicacion de los dos numeros es: ", var * var_2)
    else:
        print("El valor ingresado no coincide con las opciones")
except NameError:
    print("El programa no pudo realizar la operacion")


