# > Exercício 005

"""
Descrição:
- Escreva um programa Python que imprima a string s sem os caracteres localizados em índices pares.
- Se a string estiver vazia ou tiver apenas um caractere, imprima-a sem nenhuma alteração.

Resultado esperado:
Entrada    | Saída
""         | ""
"A"        | "A"
"Poder"    | "oe"
"Python"   | "yhn"
"Devaneio" | "eaeo"
"""

s = input("Entrada: ")

# Opção 1
saida = ""

if len(s) > 1: 
    for I in range(len(s)):
        if I % 2 != 0:
            saida += s[I]
else:
    saida = s

print(f"Saída: {saida}")

# Opção 2
saida = ""

if len(s) > 1:
    for I in range(1, len(s), 2):
        saida += s[I]
else:
    saida = s

print(f"Saída: {saida}")