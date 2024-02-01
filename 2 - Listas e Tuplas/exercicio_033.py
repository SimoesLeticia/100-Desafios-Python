# > Exercício 033

"""
Descrição:
- Escreva um programa Python que gere e imprima todas as permutações possíveis de uma lista.
- Uma permutação é uma possível disposição dos elementos da lista. Por exemplo, [2, 1, 3] é uma permutação de [1, 2, 3].
- Imprima cada permutação como uma lista em uma linha separada. 
- Inclua a própria lista como uma permutação.

Resultado esperado:
Entrada   | Saída
[1, 2, 3] | [1, 2, 3]
          | [1, 3, 2]
          | [2, 1, 3]
          | [2, 3, 1]
          | [3, 1, 2]
          | [3, 2, 1]
"""

# Entrada - Exemplo
lista_entrada = [1, 2, 3]

# Opção 1
import itertools #Esse módulo implementa diversos blocos de instruções com iteradores

lista_permutacao = list(itertools.permutations(lista_entrada))

for permutacao in lista_permutacao:
    print(f"Saída: {list(permutacao)}") # Sem utilizar o list = (1, 2, 3). Com list = [1, 2, 3]

# Opção 2
for permutacao in itertools.permutations(lista_entrada):
    print(f"Saída: {list(permutacao)}")	