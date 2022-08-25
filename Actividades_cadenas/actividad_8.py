'''Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.'''


precio = input("Ingrese el precio de un producto copn dos decimales: ")

print(f"{precio[:precio.find('.')]} pesos y {precio[precio.find('.')+1:]} centavos")


