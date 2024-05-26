# > Exercício 042

"""
Descrição:
- Escreva um programa Python que imprima a soma máxima dos valores de um dicionário.
- Assuma que todos os valores no dicionário são listas ou tuplas.

Resultado esperado:
Considerando esta entrada:
dicionario = {
    "A": [1, 2, 3],
    "B": [4, 0, -4],
    "C": [3, 5, 9],
    "D": [45, 12, 100]
}
	
A saída deve ser:
157
"""

# Entrada - Exemplo
dicionario = {
    "A": [1, 2, 3],
    "B": [4, 0, -4],
    "C": [3, 5, 9],
    "D": [45, 12, 100]
}

soma_maxima = None

for valor in dicionario.values():
	soma_atual = sum(valor)

if soma_maxima is None:
	soma_maxima = soma_atual
elif soma_maxima < soma_atual:
	soma_maxima = soma_atual

print(f"Saída: {soma_maxima}")