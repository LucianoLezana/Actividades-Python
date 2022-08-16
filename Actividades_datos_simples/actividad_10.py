payasos = int(input("Cuantos payasos queres pedir: "))
dolls = int(input("Cuantas muñecas queres pedir: "))
peso_payasos = 112 * payasos
peso_dolls = 75 * dolls

print(f"Pediste {payasos} payasos y {dolls}, el peso total del paquete es: {peso_payasos + peso_dolls}")