from matematica import he_par

numero = input("Introduce un número: ")
if he_par(int(numero)):
    print("El número es par.")
else:
    print("El número es impar.")