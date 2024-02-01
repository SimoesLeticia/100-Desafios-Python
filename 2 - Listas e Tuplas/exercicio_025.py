# > Exercício 025

"""
Descrição:
- Escreva um programa em Python que encontre a interseção de dois conjuntos (conjunto_1 e conjunto_2).
- Crie um novo conjunto chamado conjunto_intersecao que comtemple a interseção entre eles.
- Imprima o conjunto_intersecao como saída.
- Se a interseção estiver vazia, imprima um conjunto vazio.

Resultado esperado:
conjunto_1   | conjunto_2   | Saída
{1, 2, 3}    | {4, 5, 6}    | {}
{1, 2, 3}    | {3, 4, 5}    | {3}
{1, 2, 3, 4} | {3, 4, 5, 6} | {3, 4}
{1, 2, 3, 4} | {1, 2, 3, 4} | {1, 2, 3, 4}
"""

# Entrada - Exemplo
conjunto_1 = {1, 2, 3, 4} 
conjunto_2 = {3, 4, 5, 6}

# Opção 1
conjunto_intersecao = set()

for elemento in conjunto_1:
    if elemento in conjunto_2:
        conjunto_intersecao.add(elemento)      

print(f"Saída: {conjunto_intersecao}")

# Opção 2
if conjunto_1: # Para utilizar .intersection o conjunto não pode estar vazio
    conjunto_intersecao = conjunto_1.intersection(conjunto_2)
    print(f"Saída: {conjunto_intersecao}")