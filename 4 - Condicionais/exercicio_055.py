# > Exercício 055

"""
Descrição:
- Escreva um programa Python que determine se o ano fornecido é bissexto ou não.
- Se o ano fornecido for bissexto, o programa deverá imprimir "<ano> é um ano bissexto", caso contrário, o programa deverá imprimir "<ano> não é um ano bissexto".
- O ano bissexto acontece a cada quatro anos e tem duração de 366 dias. A inclusão de um dia foi feita para aproximar o calendário ao movimento de translação da Terra. Essas horas que ultrapassam os 365 dias são compensadas a cada quatro anos, no dia 29 de fevereiro.

- Para determinar se um ano é bissexto, utilizamos as seguintes regras:
    - Um ano é bissexto se for divisível por 4.
    - Porém, se o ano for divisível por 100, ele não é bissexto, a menos que:
    - O ano também seja divisível por 400, nesse caso, ele é bissexto.

Resultado esperado:
Entrada | Saída
2025    | 2025 não é um ano bissexto
2028    | 2028 é um ano bissexto
2033    | 2033 não é um ano bissexto
1836    | 1836 é um ano bissexto
1912    | 1912 é um ano bissexto
"""

# Entrada - Exemplo
ano = int(input("Entrada: "))

# Opção 1
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")

# Opção 2
if ano % 4 != 0:
    print(f"{ano} não é um ano bissexto")
elif ano % 100 != 0:
    print(f"{ano} é um ano bissexto")
elif ano % 400 != 0:
    print(f"{ano} não é um ano bissexto")
else:
    print(f"{ano} é um ano bissexto")