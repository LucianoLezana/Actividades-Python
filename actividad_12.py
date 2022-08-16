barras_no_frescas = int(input("Cuantas barras de pan quiere (recuerde no son frescas): "))
barras_pan = barras_no_frescas * 3.49
barras_pan_desc = barras_pan * 0.6
coste_final = barras_pan - barras_pan_desc
print(f"El precio habitual de una barra de pan fresca es de {barras_pan:.2f}$, al no ser fresca se le hace un descuento del {barras_pan_desc:.2f}$ el coste final es de {coste_final:.2f}$") 