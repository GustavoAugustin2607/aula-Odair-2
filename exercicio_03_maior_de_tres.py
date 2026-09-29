# Exercício 3: Parâmetros e Condicionais (Maior de Três)


def encontrar_maior(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Código principal
try:
    n1 = int(input("Primeiro número inteiro: "))
    n2 = int(input("Segundo número inteiro: "))
    n3 = int(input("Terceiro número inteiro: "))
    maior = encontrar_maior(n1, n2, n3)
    print("Maior valor:", maior)
except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")
