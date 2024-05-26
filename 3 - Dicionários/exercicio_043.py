# > Exercício 043

"""
Descrição:
- Escreva um programa Python que crie e exiba um dicionário que mapeie cada caractere de uma string conforme a frequência que ele ocorre na string.
- O dicionário deve incluir apenas os caracteres da string. 
- O teste não deve diferenciar maiúsculas de minúsculas ("A" deve ser contado como "a").
- As chaves do dicionário devem ser letras minúsculas.
- Incluir apenas letras no dicionário.

Resultado esperado:
Entrada       | Saída
Hello, World! | {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
#0l@, Mund0!  | {'l': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
Necessidade   | {'n': 1, 'e': 3, 'c': 1, 's': 2, 'i': 1, 'd': 2, 'a': 1}
"""

# Entrada - Exemplo
entrada = "#0l@, Mund0!"

# Opção 1
dicionario_frequencia = {}

for char in entrada.lower():
	if char.isalpha():
		if char in dicionario_frequencia:
			dicionario_frequencia[char] += 1
		else:
			dicionario_frequencia[char] = 1

print(f"Saída: {dicionario_frequencia}")

# Opção 2
dicionario_frequencia = {}

# isalpha = Verifica se todos os caracteres de uma string são letras
# filter  = filtra elementos de uma sequência com base em uma função específica
entrada_convertida = ''.join(filter(str.isalpha, entrada.lower()))

for char in entrada_convertida:
	if char in dicionario_frequencia:
		dicionario_frequencia[char] += 1
	else:
		dicionario_frequencia[char] = 1
		
print(f"Saída: {dicionario_frequencia}")