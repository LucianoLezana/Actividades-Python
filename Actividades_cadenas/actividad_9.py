'''Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.'''


fecha = input("Introduzca la fecha con este formato dia/mes/año: ")

print(f"Naciste el dia {fecha[:fecha.find('/')]} en el mes {fecha.find('/'):} del año ")