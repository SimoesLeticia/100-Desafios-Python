# > Exercício 015

"""
Descrição:
- Escreva um programa em Python que imprima o número de caracteres repetidos na string s.
- O programa deve imprimir o número total de caracteres repetidos acompanhado de uma mensagem exibindo os caracteres repetidos separados por espaço e ordenados alfabeticamente.
- Se não houver caracteres repetidos na string, o programa deverá imprimir 0 como a contagem total acompanhado de uma mensagem "Sem caracteres repetidos".

Resultado esperado:
Entrada    | Saída
sucesso    | 1 "s"
Corporação | 2 "o r"
Fracassar  | 3 "a r s"
Python     | 0 "Sem caracteres repetidos"
"""
s = input("Entrada: ")

caracteres_repetidos = []

# Adiciona os caracteres repetidos há uma lista
for char in s:
	if (s.count(char) > 1) and (char not in caracteres_repetidos):
		caracteres_repetidos.append(char)

# número de caracteres repetidos = quantidade de caracteres na lista
quantidade_repetidos = len(caracteres_repetidos)

if caracteres_repetidos:	
	print(f"Saída: {quantidade_repetidos} {" ".join(sorted(caracteres_repetidos))}") # Também poderia ser usado *sorted(caracteres_repetidos)
else:
	print(f"Saída: {quantidade_repetidos} Sem caracteres repetidos")