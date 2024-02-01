# > Exercício 002

"""
Descrição:
- Escreva um programa Python que imprima o caractere no índice I da string s.
- Se o índice estiver fora do intervalo ou for um número negativo, o programa deverá imprimir "Índice fora do intervalo".
- Se a string estiver vazia, o programa deverá imprimir "String vazia".

Resultado esperado:
Se a string = "Ideia" e I =  2, a saída deverá ser "e".
Se a string = "Pizza" e I =  4, a saída deverá ser "a".
Se a string = "Mundo" e I = 15, a saída deverá ser "Índice fora do intervalo".
Se a string = ""      e I =  3, a saída deverá ser "String vazia".
"""

# Entrada - Exemplo
s = "Pizza"
I = 4

if not s: # Também poderia ser usado len(s) == 0
    resultado = "String vazia"
elif I < 0 or I >= len(s):
    resultado = "Índice fora do intervalo"
else:
    resultado = s[I]

print(f"Entrada = {s}. Índice = {I}. Saída = {resultado}")