# > Exercício 050

"""
Descrição:
- Escreva um programa Python que imprima a estação do ano correspondente ao valor inteiro fornecido.
- Considere os valores possíveis: 1 para primavera, 2 para verão, 3 para outono e 4 para inverno.
- Se o valor fornecido não for nenhum desses valores, o programa deverá imprimir "Por favor, insira um valor válido".

Resultado esperado:
Entrada | Saída
1       | Primavera
2       | Verão
3       | Outono
4       | Inverno
999     | Por favor, insira um valor válido
"""

# Entrada - Exemplo
entrada = int(input("Entrada: "))

if entrada == 1:
    print("Saída: Primavera")
elif entrada == 2:
    print("Saída: Verão")
elif entrada == 3:
    print("Saída: Outono")
elif entrada == 4:
    print("Saída: Inverno")
else:
    print("Saída: Por favor, insira um valor válido")