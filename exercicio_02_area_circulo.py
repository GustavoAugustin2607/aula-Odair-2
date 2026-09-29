# Exercício 2: Calculadora de Área de Círculo

import math


def calcular_area_circulo(raio):
    return math.pi * raio ** 2


# Código principal
try:
    raio = float(input("Raio: ").replace(",", "."))
    if raio >= 0:
        area = calcular_area_circulo(raio)
        print(f"Área do círculo: {area:.2f}")
    else:
        print("O raio não pode ser negativo.")
except ValueError:
    print("Entrada inválida. Digite um número.")
