# > Exercício 035

"""
Descrição:
- Escreva um programa Python que adicione um novo par Chave-Valor a um dicionário.
- Se o par Chave-Valor já existir no dicionário, não atualize o valor existente. O dicionário não deve ser modificado neste caso.
- Armazene a nova chave na variável nova_chave e o novo valor na variável novo_valor.
- O programa deve imprimir a versão final do dicionário.

Resultado esperado:
Entrada                                       | Chave-Valor   | Saída
{"Janeiro": 45, "Fevereiro": 55, "Março": 65} | "Abril": 75   | {"Janeiro": 45, "Fevereiro": 55, "Março": 65, "Abril": 75}
{"Janeiro": 45, "Fevereiro": 55, "Março": 65} | "Janeiro": 45 | {"Janeiro": 45, "Fevereiro": 55, "Março": 65}
"""

# Entrada - Exemplo
dicionario_entrada = {"Janeiro": 45, "Fevereiro": 55, "Março": 65}
nova_chave = "Abril"
novo_valor = 75

if nova_chave not in dicionario_entrada:
	dicionario_entrada[nova_chave] = novo_valor

print(f"Saída: {dicionario_entrada}")