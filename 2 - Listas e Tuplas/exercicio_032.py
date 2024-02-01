# > Exercício 032

"""
Descrição:
- Escreva um programa em Python que imprima uma versão "achatada" de uma lista que contém listas aninhadas.
- "Achatada" significa que todos os elementos nas listas aninhadas devem ser adicionados a uma lista principal, de modo que ela não contenha mais listas aninhadas, apenas os elementos individuais.
- A lista pode conter outros elementos que não sejam listas ou outras sequências, portanto você deve verificar o tipo de cada elemento e agir adequadamente.
- Se a lista estiver vazia, imprima uma lista vazia.

Resultado esperado:
Entrada                            | Saída
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]  | [1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, [7, 8, 9]]      | [1, 2, 3, 4, 5, 6, 7, 8, 9]
[["a", "b"], "c", ["d", "e"], "f"] | ["a", "b", "c", "d", "e", "f"]
[]                                 | []
"""

# Entrada - Exemplo
lista_entrada = [["a", "b"], "c", ["d", "e"], "f"]

# Opção 1
lista_achatada = []

for elemento in lista_entrada:
	if isinstance(elemento, list): # isinstance verifica se o elemento é uma instância de uma classe ou de uma tupla de classes
		for elemento_aninhado in elemento:
			lista_achatada.append(elemento_aninhado)
	else:
		lista_achatada.append(elemento)

print(f"Saída: {lista_achatada}")

# Opção 2
lista_achatada = []

for elemento in lista_entrada:
	if isinstance(elemento, list): # isinstance verifica se o elemento é uma instância de uma classe ou de uma tupla de classes
		lista_achatada.extend(elemento) # extend é usado para concatenar listas
	else:
		lista_achatada.append(elemento)

print(f"Saída: {lista_achatada}")