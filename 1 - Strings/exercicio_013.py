# > Exercício 013

"""
Descrição:
- Escreva um programa Python que verifique se a string s termina com a sequência de caracteres indicada pela variável sufixo.
- Se a string terminar com a sequência de caracteres indicada pela variável sufixo, o programa deverá imprimir "True". Caso contrário, o programa deverá imprimir "False".
- O programa deve ser sensível a maiúsculas e minúsculas. Por exemplo, "A" não deve ser equivalente a "a".
- Se o comprimento da variável sufixo for maior que o comprimento da string, o programa deverá imprimir "False".

Resultado esperado:
Entrada          | Sufixo     | Saída
""               | "A"        | False
"Python"         | "on"       | True
"Olá, Mundo!"    | "ndo!"     | True
"Olá, Mundo!"    | "ndo"      | False
"poder"          | "poderoso" | False
"""

# Entrada - Exemplo
s      = "Python"
sufixo = "on"

# Opção 1
saida   = s[-len(sufixo):] == sufixo

print(f"Entrada = {s}. Sufixo = {sufixo}. Saída = {saida}")

# Opção 2
saida = s.endswith(sufixo)

print(f"Entrada = {s}. Sufixo = {sufixo}. Saída = {saida}")