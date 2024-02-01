# > Exercício 019

"""
Descrição:
- Escreva um programa Python que imprima o maior e o menor valor de uma lista.
- Imprima os dois valores na mesma linha, separados por um espaço.
- Imprima os valores em ordem decrescente. Ou seja, o valor mais alto deve ser mostrado primeiro.
- Assuma que a lista contém apenas valores numéricos.
- Se a lista estiver vazia, imprima a mensagem "Lista vazia".

Resultado esperado:
Entrada          | Saída
[10, 12, 14, 16] | 10 16
[-1, -2, -3, -4] | -1 -4
[0, 0, 0, 0]     | 0 0
[]               | Lista vazia
"""

# Entrada - Exemplo
lista_entrada = [-1, -2, -3, -4]

if not lista_entrada:
    print("Saída: Lista vazia")
else:
    print(f"Saída: {max(lista_entrada)} {min(lista_entrada)}")