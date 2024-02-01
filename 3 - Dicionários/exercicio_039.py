# > Exercício 039

"""
Descrição:
- Escreva um programa Python que imprime o menor valor presente em um dicionário.
- Se o dicionário estiver vazio, o programa deve imprimir "Dicionário vazio".
- Assuma que os valores são numéricos.

Resultado esperado:
Entrada                     | Saída
{"A": 50, "B": 51, "C": 49} | 49
{"A": -1, "B": -2, "C": -3} | -3
{"A": 12, "B": 12, "C": 12} | 12
{}                          | "Dicionário vazio"
"""

# Entrada - Exemplo
dicionario_entrada = {"A": -1, "B": -2, "C": -3}

if not dicionario_entrada:
    print("Dicionário vazio")
else:
    menor_valor = min(dicionario_entrada.values())
    print(f"Saída: {menor_valor}")