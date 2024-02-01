# > Exercício 028

"""
Descrição:
- Escreva um programa Python que imprima uma lista com os elementos que Lista_A e Lista_B têm em comum.
- Se eles não tiverem nenhum elemento em comum, imprima uma lista vazia.
- As listas podem ter comprimentos diferentes.
- Assuma que cada elemento aparecerá apenas uma vez em cada lista.

Resultado esperado:
Lista_A   | Lista_B   | Saída
[1, 2, 3] | [1, 2, 3] | [1, 2, 3]
[4, 5, 6] | [1, 4, 5] | [4, 5]
[3, 4, 5] | [1, 2, 3] | [3]
[4, 5, 6] | [7, 8, 9] | []
"""

# Entrada - Exemplo
lista_a = [4, 5, 6]
lista_b = [1, 4, 5]

# Opção 1
elementos_comuns = []

for elemento in lista_a:
	if elemento in lista_b:
		elementos_comuns.append(elemento)
		
print(f"Saída: {elementos_comuns}")

# Opção 2
elementos_comuns = list(set(lista_a) & set(lista_b)) # Operador '&' realiza a interseção entre as listas

print(f"Saída: {elementos_comuns}")