# > Exercício 044

"""
Descrição:
- Escreva um programa Python que classifique em ordem crescente as listas contidas como valores em um dicionário.
- O dicionário contém pares de chave-valor que associam strings a listas. É necessário ordenar essas listas.
- As listas devem ser alteradas.

Resultado esperado:
Considerando esta entrada:
dicionario = {
    "A": [4, 3, 2],
    "B": [5, 3, 7],
    "C": [1, 9, 10],
    "D": [3, 4, 1]
}

A saída deve ser:
dicionario = {
    "A": [2, 3, 4],
    "B": [3, 5, 7],
    "C": [1, 9, 10],
    "D": [1, 3, 4]
}
"""

# Entrada - Exemplo
dicionario = {
    "LISTA_A": [3, 1, 2],
    "LISTA_B": [6, 5, 4],
    "LISTA_C": [9, 7, 8]
}

# Opção 1
for lista in dicionario.values():
    lista.sort()

print(f"Saída: {dicionario}")	

# Opção 2
for chave in dicionario:
    dicionario[chave].sort()

print(f"Saída: {dicionario}")    