# > Exercício 026

"""
Descrição:
- Escreva um programa em Python que encontre a diferença de dois conjuntos (conjunto_1 e conjunto_2). Ou seja, os elementos de conjunto_1 que não estão presentes em conjunto_2.
- Crie um novo conjunto chamado conjunto_diferenca que contemple os elementos de conjunto_1 que não estão presentes em conjunto_2.
- Imprima o conjunto_diferenca como saída.
- Se conjunto_1 e conjunto_2 possuírem os mesmos elementos, imprima uma lista vazia.
- Se conjunto_1 for uma lista vazia, imprima uma lista vazia.

Resultado esperado:
conjunto_1   | conjunto_2   | Saída
[1, 2, 3, 4] | [1, 2]       | [3, 4]
[5, 6, 7, 8] | [5, 6, 7]    | [8]
[2, 4, 6, 8] | [2, 4, 6, 8] | []
[]           | [7, 9]       | []
"""

# Entrada - Exemplo
conjunto_1 = [1, 2, 3, 4]
conjunto_2 = [1, 2]

# Opção 1
conjunto_diferenca = []

for elemento in conjunto_1:
	if elemento not in conjunto_2:
		conjunto_diferenca.append(elemento)

print(f"Saída: {conjunto_diferenca}")

# Opção 2

conjunto_diferenca = list(set(conjunto_1) - set(conjunto_2))

print(f"Saída: {conjunto_diferenca}")


