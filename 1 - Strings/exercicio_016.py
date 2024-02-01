# > Exercício 016

"""
Descrição:
- Escreva um programa Python que converta uma string s em minúsculas e classifique os caracteres de cada palavra em ordem alfabética.
- Assuma que a string contenha apenas letras.
- Assuma que espaços sejam usados para separar as palavras.
- Os espaços devem ser preservados na string final.

Resultado esperado:
Entrada                       | Saída
Hello World                   | ehllo dlorw
Pequenos Passos Todos os Dias | eenopqsu aopsss doost os adis
Eu amo Python                 | eu amo hnopty
"""

s = input("Entrada: ")

# Opção 1
saida = ""

lista_palavras = s.split(" ")

for palavra in lista_palavras:
	saida += "".join(sorted(palavra.lower())) + " "

saida.rstrip()

print(f"Saída: {saida}")

# Opção 2
lista_palavras_ordenadas = []
lista_palavras = s.split(" ")

for palavra in lista_palavras:
    lista_palavras_ordenadas.append("".join(sorted(palavra.lower()))) # Armazena as palavras ordenadas e minúsculas numa nova lista

saida = " ".join(lista_palavras_ordenadas) # Reune as palavras de volta numa única string

print(f"Saída: {saida}")