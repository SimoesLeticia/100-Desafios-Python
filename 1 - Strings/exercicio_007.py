# > Exercício 007

"""
Descrição:
- Escreva um programa em Python que imprima a string s sem o caractere no índice n.
- Se a string estiver vazia ou o índice n estiver fora do intervalo, imprima-a sem nenhuma alteração.

Resultado esperado:
Entrada  | n  | Saída
""       | 2  | ""
"Olá"    | 15 | "Olá"
"Poder"  | 1  | "Pder"
"Python" | 3  | "Pyton"
"""

# Entrada - Exemplo
s = "Python"
n = 3

# Opção 1
if (not s) or (n >= len(s)):
    print(s)
else:
    saida = ""
    for I in range(len(s)):
        if I != n:
            saida += s[I]
    print(f"Entrada = {s}. Índice = {n}. Saída = {saida}")

# Opção 2
if (not s) or (n >= len(s)):
    print(s)
else:
    saida = s[:n] + s[n+1:]
    print(f"Entrada = {s}. Índice = {n}. Saída = {saida}")