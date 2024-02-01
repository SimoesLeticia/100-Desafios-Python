# > Exercício 009

"""
Descrição:
- Escreva um programa Python que imprima a string s com todas as vírgulas substituídas por pontos.

Resultado esperado:
Entrada       | Saída
""            | ""
"Olá, Mundo!" | "Olá. Mundo!"
"3,333,333"   | "3.333.333"
"""

s       = input("Entrada: ")
virgula = ","
ponto   = "."

# Opção 1
saida = ""

for char in s:
    if char == virgula:
        saida += ponto
    else:
        saida += char

print(f"Entrada = {s}. Saída = {saida}")

# Opção 2
saida = s.replace(virgula, ponto)

print(f"Entrada = {s}. Saída = {saida}")