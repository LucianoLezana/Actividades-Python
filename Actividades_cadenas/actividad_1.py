'''Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas el nombre 
del usuario tantas veces como el número introducido.'''

user_name = input("Ingrese su nombre: ")
number = int(input("Ingrese un numero entero: "))

for x in range(number):
    print(user_name)