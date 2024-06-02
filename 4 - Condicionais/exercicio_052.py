# > Exercício 052

"""
Descrição:
- Escreva um programa Python que imprima o número de dias de um determinado mês.
- O valor da variável mês é o nome do mês com a primeira letra maiúscula.
- Não considere anos bissextos para o número de dias de fevereiro.
- Adicione uma mensagem personalizada. Por exemplo: "<mês> tem <numero_dias> dias"

Resultado esperado:
Entrada   | Saída
Janeiro   | tem 31 dias
Fevereiro | tem 28 dias
Março     | tem 31 dias
Abril     | tem 30 dias
Maio      | tem 31 dias
Junho     | tem 30 dias
Julho     | tem 31 dias
Agosto    | tem 31 dias
Setembro  | tem 30 dias
Outubro   | tem 31 dias
Novembro  | tem 30 dias
Dezembro  | tem 31 dias
"""

# Entrada - Exemplo
mes = input("Entrada: ")

# Opção 1
mes_28_dias = ("Fevereiro")
mes_30_dias = ("Abril", "Junho", "Setembro", "Novembro")
mes_31_dias = ("Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro")

if mes in mes_31_dias:
    print(f"{mes} tem 31 dias")
elif mes in mes_30_dias:
    print(f"{mes} tem 30 dias")
elif mes in mes_28_dias:
    print(f"{mes} tem 28 dias")
else:
    print(f"Entrada inválida!")
    
# Opção 2
dias_no_mes = {
    "Janeiro":   31,
    "Fevereiro": 28,
    "Março":     31,
    "Abril":     30,
    "Maio":      31,
    "Junho":     30,
    "Julho":     31,
    "Agosto":    31,
    "Setembro":  30,
    "Outubro":   31,
    "Novembro":  30,
    "Dezembro":  31
}

if mes in dias_no_mes:
    print(f"{mes} tem {dias_no_mes[mes]} dias")
else:
    print(f"Entrada inválida!")