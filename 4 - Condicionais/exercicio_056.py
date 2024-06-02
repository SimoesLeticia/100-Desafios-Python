# > Exercício 056

"""
Descrição:
- Escreva um programa Python que simule uma calculadora interativa com as operações aritméticas básicas: adição, subtração, multiplicação, divisão, divisão inteira e módulo (resto da divisão).
- O programa deve interagir com o usuário solicitando os valores e o tipo de operação que será realizada.
- A saída deve incluir os valores, a operação e o resultado. Por exemplo: "O resultado de 1 + 2 é 3".

- O tipo de operação aritmética será indicado por um número inteiro.
    - 1 = Adição.
    - 2 = Subtração.
    - 3 = Multiplicação.
    - 4 = Divisão.
    - 5 = Divisão Inteira.
    - 6 = Módulo (resto da divisão)

- O programa deverá apresentar uma mensagem inicial ao usuário solicitando os valores e descrevendo as operações disponíveis.
- Se o usuário inserir um número inteiro inválido para selecionar a operação, o programa deverá imprimir "Por favor, escolha uma operação válida".
- Caso os valores informados pelo usuário sejam inválidos para a operação selecionada, uma mensagem deverá ser exibida. Por exemplo, para uma operação de divisão, o denominador não pode ser 0.

Resultado esperado:
Entrada:
=== Bem-vindo à sua calculadora Python interativa ===
Insira o primeiro valor: 16
Insira o segundo valor: 3
Selecione uma operação. Estas são as opções disponíveis:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Divisão Inteira
6 - Módulo
Insira o número da operação desejada: 6

Saída
O resultado de 16 % 3 é 1
"""

print("=== Bem-vindo à sua calculadora Python interativa ===")

# Solicita os valores e a operação ao usuário
valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))

print("Selecione uma operação. Estas são as opções disponíveis:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Divisão Inteira")
print("6 - Módulo")

operacao = int(input("Insira o número da operação desejada: "))

ADICAO          = 1
SUBTRACAO       = 2
MULTIPLICACAO   = 3
DIVISAO         = 4
DIVISAO_INTEIRA = 5
MODULO          = 6

if operacao == ADICAO:
    resultado = valor1 + valor2
    print(f"O resultado de {valor1} + {valor2} é {resultado}")
elif operacao == SUBTRACAO:
    resultado = valor1 - valor2
    print(f"O resultado de {valor1} - {valor2} é {resultado}")
elif operacao == MULTIPLICACAO:
    resultado = valor1 * valor2
    print(f"O resultado de {valor1} * {valor2} é {resultado}")
elif operacao == DIVISAO:
    if valor2 == 0:
        print("Não é possível dividir por zero. Por favor, insira um segundo valor diferente de zero.")
    else:
        resultado = valor1 / valor2
        print(f"O resultado de {valor1} / {valor2} é {resultado}")
elif operacao == DIVISAO_INTEIRA:
    if valor2 == 0:
        print("Não é possível dividir por zero. Por favor, insira um segundo valor diferente de zero.")
    else:
        resultado = valor1 // valor2
        print(f"O resultado da divisão inteira de {valor1} por {valor2} é {resultado}")
elif operacao == MODULO:
    if valor2 == 0:
        print("Não é possível realizar a operação de módulo (resto da divisão) por zero. Por favor, insira um segundo valor diferente de zero.")
    else:
        resultado = valor1 % valor2
        print(f"O resultado de {valor1} % {valor2} é {resultado}")
else:
    print("Por favor, escolha uma operação válida")