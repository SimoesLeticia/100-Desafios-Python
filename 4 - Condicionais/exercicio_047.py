# > Exercício 047

"""
Descrição:
- Escreva um programa Python que leia uma string e imprima uma mensagem descritiva para cada caractere da string. Indicando se o caractere é uma vogal ou uma consoante. Por exemplo: "<char> é <consoante | vogal>"
- Em casos de espaços, caracteres especiais, números ou símbolos, o programa deverá imprimir "<char> não é letra".
- Se a string estiver vazia, o programa deverá imprimir "String vazia".
- Converta a string para letras minúsculas antes de realizar as comparações.

Resultado esperado:
Considerando esta entrada:
Olá Mundo!
	
A saída deve ser:
o é vogal
l é consoante
à é vogal
  não é letra
m é consoante
u é vogal
n é consoante
d é consoante
o é vogal
! não é letra
"""

# Entrada - Exemplo
entrada = input("Entrada: ")

# Opção 1
vogais = "aeiouáéíóúàèìòùâêîôûãõäëïöü"

if not entrada:
    print("String vazia")
else:
    for char in entrada.lower():
        if char in vogais:
            print(f"{char} é vogal")
        elif not char.isalpha():
            print(f"{char} não é letra")
        else:
            print(f"{char} é consoante")

# Opção 2
print('\n')
vogais = "aeiouáéíóúàèìòùâêîôûãõäëïöü"
entrada = entrada.lower()

if not entrada:
    print("String vazia")
else:
    for char in entrada:
        if char.isalpha():
            if char in vogais:
                print(f"{char} é vogal")
            else:
                print(f"{char} é consoante")
        else:
            print(f"{char} não é letra")            