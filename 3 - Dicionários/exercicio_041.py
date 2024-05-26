# > Exercício 041

"""
Descrição:
- Escreva um programa em Python que crie um dicionário a partir dos valores contidos em listas aninhadas.
- Cada lista aninhada tem este formato [valor1, valor2].
- valor1 deve ser a chave no dicionário e valor2 deve ser seu valor correspondente.
- Se não houver listas aninhadas, imprima um dicionário vazio.

Resultado esperado:
Considerando esta entrada:
[["A", 1], ["B", 2], ["C", 3], ["D", 4]]
	
A saída deve ser:
{"A": 1, "B": 2, "C": 3, "D": 4}
"""

# Entrada - Exemplo
listas_aninhadas = [["A", 1], ["B", 2], ["C", 3], ["D", 4]]

# Opção 1
dicionario = {}

for lista_aninhada in listas_aninhadas:
    chave = lista_aninhada[0] 
    valor = lista_aninhada[1]
    dicionario[chave] = valor
    
print(f"Saída: {dicionario}")

# Opção 2
if not listas_aninhadas:
    dicionario = {}
else:
    dicionario = {item[0]: item[1] for item in listas_aninhadas}    
    
print(f"Saída: {dicionario}")