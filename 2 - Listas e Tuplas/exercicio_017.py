# > Exercício 017

"""
Descrição:
- Escreva um programa Python que multiplique todos os itens de uma lista pelo valor de uma variável fator.
- O programa deve permitir a multiplicação da variável fator por uma string caso a lista contenha caracteres não numéricos.
- O programa deve imprimir uma nova lista como saída.
- Assuma que o valor da variável fator será um número inteiro positivo.

Resultado esperado:
Entrada         | Fator | Saída
[3, 4, 5, 6]    | 2     | [6, 8, 10, 12]
["A", "B", "C"] | 3     | ["AAA", "BBB", "CCC"]
"""

# Entrada - Exemplo
lista_entrada = ["A", "B", "C", 3, 4, 5, 6]

fator   = 2

# Opção 1
for I in range(len(lista_entrada)):
	lista_entrada[I] *= fator

print(f"Saída: {lista_entrada}")

# Opção 2
lista_saida = []

for I, elemento in enumerate(lista_entrada):
	lista_saida.append(elemento * fator)

print(f"Saída: {lista_saida}")