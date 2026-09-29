# Exercício 1: Arredondamento e Raiz Quadrada

import math

try:
    numero = float(input("Número positivo: ").replace(",", "."))
    if numero > 0:
        print("Raiz quadrada:", math.sqrt(numero))
        print("Arredondado para cima:", math.ceil(numero))
        print("Arredondado para baixo:", math.floor(numero))
    else:
        print("Digite um número maior que zero.")
except (ValueError, OverflowError):
    print("Entrada inválida. Digite um número decimal.")
