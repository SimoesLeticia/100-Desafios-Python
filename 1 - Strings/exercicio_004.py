# > Exercício 004

"""
Descrição:
- Escreva um programa Python que imprima os três primeiros e os três últimos caracteres da string s como uma única string.
- Se a string tiver menos de seis caracteres, imprima uma string vazia (saída em branco).

Resultado esperado:
Entrada        | Saída
"Poder"        | ""
"Utopia"       | "Utopia"
"Família"      | "Famlia"
"Conhecimento" | "Connto"
"""

s = input("Entrada: ")
numero_caracteres = 3

if len(s) >= 2 * numero_caracteres:
    saida = s[:numero_caracteres] + s[-numero_caracteres:]
else:
    saida = ""

print(f"Saída: {saida}")