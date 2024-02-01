# > Exercício 034

"""
Descrição:
- Escreva um programa Python que verifique se existe ou não uma chave em um dicionário.
- Se a chave existir no dicionário, o programa deve imprimir "True". Caso contrário, o programa deve imprimir "False".

Resultado esperado:
Entrada          | Chave | Saída
{"A": 1, "B": 2} | "A"   | True
{"C": 3, "D": 4} | "F"   | False
{}               | "H"   | False
"""

# Entrada - Exemplo
dicionario_entrada = {"A": 1, "B": 2}
chave = "A"

# Opção 1
verifica_chave_dicionario = chave in dicionario_entrada

print(f"Entrada = {dicionario_entrada}. Chave = {chave}. Saída = {verifica_chave_dicionario}")

# Opção 2
print(f"Entrada = {dicionario_entrada}. Chave = {chave}. Saída = {chave in dicionario_entrada}")