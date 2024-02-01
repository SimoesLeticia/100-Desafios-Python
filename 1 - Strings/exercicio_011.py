# > Exercício 011

"""
Descrição:
- Escreva um programa Python que imprima a string s sem espaços.
- Se a string não contiver espaços, imprima-a sem nenhuma alteração.

Resultado esperado:
Entrada              | Saída
"Olá, Mundo!"        | "Olá,Mundo!"
"Tenha um ótimo dia" | "Tenhaumótimodia"
"Python"             | "Python"
"""

s = input("Entrada: ")

# Opção 1
saida = ""

for char in s:
	if char != " ":
		saida += char

print(f"Saída: {saida}")		

# Opção 2
print(f"Saída: {s.replace(" ", "")}")