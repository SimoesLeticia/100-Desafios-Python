# > Exercício 049

"""
Descrição:
- Escreva um programa Python que leia três valores inteiros separados por vírgula e armazene cada valor em uma respectiva variável. Por exemplo: 10, 12, -15 devem ser armazenados da seguinte forma:  A = 10, B = 12 e C = -15.
- O programa deverá imprimir o menor valor dentre os três valores fornecidos.

Resultado esperado:
Entrada    | Saída
10, 20, 30 | 10
1, 2, -3   | -3
5, 5, 5    | 5
"""

# Entrada - Exemplo
entrada = "10, 12, -15"

A, B, C = map(int, entrada.split(','))

# Opção 1
menor_valor = min(A, B, C)

print(f"Saída: {menor_valor}")

# Opção 2
if (A <= B) and (A <= C):
   menor_valor = A
elif (B <= A) and (B <= C):
   menor_valor = B
else:
   menor_valor = C

print(f"Saída: {menor_valor}")