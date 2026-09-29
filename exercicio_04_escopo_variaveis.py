# Exercício 4: Compreendendo Escopo de Variáveis

x = 10  # Variável 1


def alterar_valor():
    x = 5  # Variável 2
    print(f"Valor dentro da função: {x}")


alterar_valor()
print(f"Valor fora da função: {x}")

# Resposta A - Saída exata:
# Valor dentro da função: 5
# Valor fora da função: 10

# Resposta B:
# O x definido fora da função é global e vale 10. Já o x = 5 de alterar_valor() é uma
# variável local, usada apenas dentro dessa função. Essa atribuição não modifica a
# variável global, pois são variáveis de escopos diferentes, apesar de terem o
# mesmo nome. Assim, a função imprime 5 e o código principal imprime 10.
