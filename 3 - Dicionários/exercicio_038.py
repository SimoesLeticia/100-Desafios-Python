# > Exercício 038

"""
Descrição:
- Escreva um programa Python que imprime o maior valor presente em um dicionário.
- Se o dicionário estiver vazio, o programa deve imprimir "Dicionário vazio".
- Você pode assumir que os valores são numéricos.

Resultado esperado:
Entrada                     | Saída
{"A": 50, "B": 51, "C": 49} | 51
{"A": -1, "B": -2, "C": -3} | -1
{"A": 12, "B": 12, "C": 12} | 12
{}                          | "Dicionário vazio"
"""

# Entrada - Exemplo
dicionario_entrada = {"A": -1, "B": -2, "C": -3}

if not dicionario_entrada:
    print("Dicionário vazio")
else:
    maior_valor = max(dicionario_entrada.values())
    print(f"Saída: {maior_valor}")