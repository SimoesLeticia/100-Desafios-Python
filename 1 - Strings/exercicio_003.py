# > Exercício 003

"""
Descrição:
- Escreva um programa Python que imprima a versão invertida de uma string.
- O programa deve preservar letras maiúsculas e minúsculas.
- Se a string estiver vazia, imprima-a sem nenhuma alteração.

Resultado esperado:
Entrada  | Saída
""       | ""
"Wo"     | "oW"
"Olá"    | "álO"
"radar"  | "radar"
"""

s = input("Entrada: ")

# Opção 1
string_invertida = s[::-1]
print(f"Saída: {string_invertida}")

# Opção 2
string_invertida = "".join(reversed(s))
print(f"Saída: {string_invertida}")