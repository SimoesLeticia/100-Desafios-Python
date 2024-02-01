# > Exercício 024

"""
Descrição:
- Escreva um programa Python que conte o número de elementos em uma lista com valor maior que a variável n.
- Assuma que a lista contém apenas números inteiros.
- O programa deverá imprimir a contagem final.

Resultado esperado:
Entrada           | n  | Saída
[-2, -1, 0, 1, 2] | 5  | 0
[1, 2, 3, 4]      | 3  | 1
[10, 11, 12, 13]  | 8  | 4
[]                | 12 | 0
"""

# Entrada - Exemplo
lista_entrada = [1, 2, 3, 4]  
n             = 3

# Opção 1
contador = 0

for elemento in lista_entrada:
	if elemento > n:
		contador += 1
		
print(f"Saída: {contador}")

# Opção 2
contador = sum(1 for elemento in lista_entrada if elemento > n)

print(f"Saída: {contador}")

# Opção 3
contador = len([1 for elemento in lista_entrada if elemento > n])

print(f"Saída: {contador}")
