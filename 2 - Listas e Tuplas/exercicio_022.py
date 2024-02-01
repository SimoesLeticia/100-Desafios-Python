# > Exercício 022

"""
Descrição:
- Escreva um programa Python que remova todas as ocorrências do elemento n de uma lista.
- A saída do programa deve ser a nova lista com o elemento removido.
- Caso o elemento não seja encontrado na lista, imprima a mensagem "Elemento não encontrado".
- Se a lista estiver vazia, imprima a mensagem "Lista vazia".

Resultado esperado:
Entrada              | n   | Saída
[1, 2, 3, 4]         | 2   | [1, 3, 4]
[6, 6, 7, 8]         | 6   | [7, 8]
["A", "B", "C", "B"] | "B" | ["A", "C"]
[19, 18, 17, 16]     | 13  | Elemento não encontrado
[]                   | 0   | Lista vazia
"""

# Entrada - Exemplo
n             = "D"
lista_entrada = [1, 2, 3, 3, 4, 5, 6, 3, 7, 3, 3, 8, 9, 10] # Saída = [1, 2, 4, 5, 6, 7, 8, 9, 10]

if not lista_entrada:
	print("Saída: Lista vazia")
elif n not in lista_entrada: # Também poderia ser usado lista_entrada.count(n) == 0
	print("Saída: Elemento não encontrado")
else:	
	for I in range(lista_entrada.count(n)):
		lista_entrada.remove(n)		
	print(f"Saída: {lista_entrada}")