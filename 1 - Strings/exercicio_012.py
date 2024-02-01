# > Exercício 012

"""
Descrição:
- Escreva um programa Python que verifique se a string s começa com a sequência de caracteres indicada pela variável prefixo.
- Se a string começa com a sequência de caracteres indicada pela variável prefixo, o programa deverá imprimir "True". Caso contrário, o programa deverá imprimir "False".
- O programa deve ser sensível a maiúsculas e minúsculas. Por exemplo, "A" não deve ser equivalente a "a".
- Se o comprimento da variável prefixo for maior que o comprimento da string, o programa deverá imprimir "False".

Resultado esperado:
Entrada          | Prefixo    | Saída
""               | "Python"   | False
"Olhe para trás  | "Ol"       | True
"Olá, Mundo!"    | "Ol"       | True
"Olá, Mundo!"    | "ol"       | False
"poder"          | "poderoso" | False
"""

# Entrada - Exemplo
s       = "Olá, Mundo!"
prefixo = "Ol"

# Opção 1
saida   = s[:len(prefixo)] == prefixo

print(f"Entrada = {s}. Prefixo = {prefixo}. Saída = {saida}")

# Opção 2
saida = s.startswith(prefixo)

print(f"Entrada = {s}. Prefixo = {prefixo}. Saída = {saida}")