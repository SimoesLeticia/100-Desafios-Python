# > Exercício 051

"""
Descrição:
- Escreva um programa Python que leia três valores inteiros separados por vírgula e armazene cada valor em uma respectiva variável. Por exemplo: 10, 10, 10 devem ser armazenados da seguinte forma: A = 10, B = 10 e C = 10. 
- Se os três valores fornecidos forem todos iguais, o programa deverá imprimir "São iguais". Caso contrário, se pelo menos um valor fornecido for diferente dos outros, o programa imprimirá "Não são iguais".

Resultado esperado: 
Entrada    | Saída 
10, 20, 30 | Não são iguais 
55, 55, 56 | Não são iguais 
99, 99, 99 | São iguais
"""

# Entrada - Exemplo
entrada = "99, 99, 99"

A, B, C = map(int, entrada.split(','))

# Opção 1
if (A == B) and (B == C):
    print("Saída: São iguais")
else:
    print("Saída: Não são iguais")

# Opção 2
if A == B == C:
    print("Saída: São iguais")
else:
    print("Saída: Não são iguais")