# > Exercício 031

"""
Descrição:
- Escreva um programa Python que crie e imprima um dicionário que mapeie cada elemento de uma lista e sua frequência correspondente, ou seja, quantas vezes ele ocorre na lista.
- O programa deve diferenciar maiúsculas de minúsculas. Portanto, “A” não deve ser considerado o mesmo que “a”.

Resultado esperado:
Entrada                             | Saída
["a", "a", "b", "c", "D", "a", "b"] | ["a": 3, "b": 2, "c": 1, "D": 1]
[1, 2, 3, 4, 3, 2, 1, 2, 4, 4, 4]   | [1: 2, 2: 3, 3: 2, 4: 4]
"""

# Entrada - Exemplo
lista_entrada = ["a", "a", "b", "c", "D", "a", "b"] 

dicionario_frequencia = {}

for elemento in lista_entrada:
	if elemento not in dicionario_frequencia:
		dicionario_frequencia[elemento] = 1
	else:
		dicionario_frequencia[elemento] += 1

print(f"Saída: {dicionario_frequencia}")