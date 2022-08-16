cant_invertir = float(input("Ingrese la cantidad a invertir: "))
int_anual = float(input("ingrese el interes anual: "))
anios_a_invertir = float(input("Ingrese cuantos años quiere invertir: "))

cap_obtenido = cant_invertir * (int_anual/ 100 + 1) ** anios_a_invertir

print(f"El capital obtenido es de: {cap_obtenido:.2f} ")