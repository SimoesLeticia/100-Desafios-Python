# > Exercício 006

"""
Descrição:
- Escreva um programa Python que verifique se uma string contém apenas números.
- Se a string contém apenas números, o programa deverá imprimir "True". Caso contrário, o programa deverá imprimir "False".

Resultado esperado:
Entrada | Saída
""      | False
"Olá"   | False
"1234"  | True
"-1.5"  | False
"""

s = input("Entrada: ")

saida = s.isnumeric() # Também poderia ser usado s.isdecimal()

print(f"Saída: {saida}")