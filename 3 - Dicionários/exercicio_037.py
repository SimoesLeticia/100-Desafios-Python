# > Exercício 037

"""
Descrição:
- Escreva um programa Python que verifique se todos os valores em um dicionário são iguais.
- Se todos os valores do dicionário forem iguais o programa deve imprimir "True". Caso contrário, imprima "False".
- Se o dicionário estiver vazio, o programa deve imprimir "Dicionário vazio".


Resultado esperado:
Entrada                  | Saída
{"A": 7, "B": 7, "C": 7} | True
{"A": 1, "B": 1, "C": 2} | False
{"A": 1, "B": 2, "C": 3} | False
{}                       | "Dicionário vazio"
"""

# Entrada - Exemplo
dicionario_entrada = {"A": 7, "B": 7, "C": 7}

numero_valores_iguais = len(set(dicionario_entrada.values()))

if numero_valores_iguais == 0:
     print("Dicionário vazio")
elif numero_valores_iguais == 1:
     print(f"Saída: {True}")
else:
     print(f"Saída: {False}")