# > Exercício 053

"""
Descrição:
- Escreva um programa Python que leia três valores inteiros separados por vírgula e armazene cada valor em uma respectiva variável. Por exemplo: 10, 11, 12 devem ser armazenados da seguinte forma:  A = 10, B = 11 e C = 12.
- O programa deverá determinar se os números fornecidos estão em ordem crescente, decrescente ou em nenhuma ordem específica.

Resultado esperado:
Entrada | Saída
1, 2, 3 | Ordem crescente
3, 2, 1 | Ordem decrescente
1, 2, 1 | Nenhuma
1, 1, 1 | Nenhuma
"""

# Entrada - Exemplo
entrada = "-1, 0, 1"

A, B, C = map(int, entrada.split(','))

# Opção 1
if A > B > C:
    print("Ordem decrescente")
elif A < B < C:
    print("Ordem crescente")
else:
    print("Nenhuma")