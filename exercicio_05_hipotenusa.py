# Exercício 5: Desafio Integrador (Cálculo de Hipotenusa)

# 1. Imports
import math


# 2. Funções
def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)


# 3. Código principal
try:
    a = float(input("Cateto a: ").replace(",", "."))
    b = float(input("Cateto b: ").replace(",", "."))
    if a > 0 and b > 0:
        hipotenusa = calcular_hipotenusa(a, b)
        print("Hipotenusa:", hipotenusa)
    else:
        print("Os catetos devem ser maiores que zero.")
except ValueError:
    print("Entrada inválida. Digite um número.")
