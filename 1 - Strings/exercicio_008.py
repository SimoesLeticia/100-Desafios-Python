# > Exercício 008

"""
Descrição:
- Escreva um programa Python que imprima a string s com o caractere caractere_atual substituído pelo caractere caractere_novo.
- caractere_atual e caractere_novo são variáveis que contêm strings com um único caractere.
- Assuma que caractere_novo não será uma string vazia.
- A correspondência deve ser sensível a maiúsculas e minúsculas (não substitua letras minúsculas se caractere_atual for maiúsculo)
- Se nenhuma correspondência for encontrada, imprima a string inicial sem nenhuma alteração.

Resultado esperado:
Entrada   | caractere_atual | caractere_novo | Saída
"assunto" | "s"             | "l"            | "allunto"
"Nunca"   | "N"             | "A"            | "Aunca"
"Python"  | "P"             | "x"            | "xython"
"Python"  | "p"             | "z"            | "Python"
"""

# Entrada - Exemplo
s               = "Nunca"
caractere_atual = "N"
caractere_novo  = "A"

# Opção 1
saida = ""

for char in s:
    if char == caractere_atual:
        saida += caractere_novo
    else:
        saida += char

print(f"Entrada = {s}. caractere_atual = {caractere_atual}. caractere_novo = {caractere_novo}. Saída = {saida}")

# Opção 2
saida = s.replace(caractere_atual, caractere_novo)

print(f"Entrada = {s}. caractere_atual = {caractere_atual}. caractere_novo = {caractere_novo}. Saída = {saida}")