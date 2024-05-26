# > Exercício 045

"""
Descrição:
- Escreva um programa Python que leia o conteúdo de um dicionário e o converta em uma lista de listas.
- Cada lista aninhada deve conter uma chave como primeiro elemento e seu valor correspondente como segundo elemento.
- Imprima a lista final de listas.

Resultado esperado:
Considerando esta entrada:
produto_info = {
    "descrição": "sapato",
	"preço": 37.99,
	"cores": ["amarelo", "azul", "vermelho"],
}

A saída deve ser:
[['descrição', 'sapato'], ['preço', 37.99], ['cores', ['amarelo', 'azul', 'vermelho']]]
"""

# Entrada - Exemplo
produto_info = {
    "descrição": "sapato",
	"preço": 37.99,
	"cores": ["amarelo", "azul", "vermelho"],
}

lista_de_listas = []

for chave, valor in produto_info.items():
    lista_de_listas.append([chave, valor])

print(f"Saída: {lista_de_listas}")