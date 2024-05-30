# > Exercício 048

"""
Descrição:
- Escreva um programa Python que leia três valores inteiros separados por vírgula e armazene cada valor em uma respectiva variável. Por exemplo: 10, 12, -15 devem ser armazenados da seguinte forma:  A = 10, B = 12 e C = -15.
- O programa deverá imprimir o maior valor dentre os três valores fornecidos.

Resultado esperado:
Entrada    | Saída
10, 20, 30 | 30
1, 2, -3   | 2
5, 5, 5    | 5
"""

# Entrada - Exemplo
entrada = "10, 12, -15"

A, B, C = map(int, entrada.split(','))

# Opção 1
maior_valor = max(A, B, C)

print(f"Saída: {maior_valor}")

# Opção 2
if (A >= B) and (A >= C):
   maior_valor = A
elif (B >= A) and (B >= C):
   maior_valor = B
else:
   maior_valor = C

print(f"Saída: {maior_valor}")