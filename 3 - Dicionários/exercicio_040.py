# > Exercício 040

"""
Descrição:
- Escreva um programa Python que conte a frequência de cada valor em um dicionário.
- O programa deve criar um novo dicionário para mapear cada valor do dicionário original para sua frequência (quantas vezes ele ocorre).
- Se o dicionário estiver vazio, imprima um dicionário vazio.

Resultado esperado:
Considerando esta entrada:
dicionario_entrada = {
	"A": 4,
	"B": 4,
	"C": 2,
	"D": 7,
	"E": 4,
	"F": 2,
	"G": 7,
	"H": 7
}
	
A saída deve ser:
dicionario_frequencia = {
	4: 3,
	2: 2,
	7: 3
}

Cada valor em dicionario_entrada é uma chave em dicionario_frequencia e é mapeado para sua frequência correspondente como valor.
"""

# Entrada - Exemplo
dicionario_entrada = {
    "A": 4,
    "B": 4,
    "C": 2,
    "D": 7,
    "E": 4,
    "F": 2,
    "G": 7,
    "H": 7
}

# Opção 1
dicionario_frequencia = {}

for valor in dicionario_entrada.values():
	if valor in dicionario_frequencia:
		dicionario_frequencia[valor] += 1
	else:
		dicionario_frequencia[valor] = 1

print(f"Saída: {dicionario_frequencia}")

# Opção 2
dicionario_frequencia = {}

for valor in dicionario_entrada.values():
    dicionario_frequencia[valor] = dicionario_frequencia.get(valor, 0) + 1
	
print(f"Saída: {dicionario_frequencia}")