# > Exercício 036

"""
Descrição:
- Escreva um programa Python que mescle dois dicionários e imprima o dicionário resultante.
- "Mesclar" os dicionários envolve criar um novo dicionário com os pares de valores-chave em ambos os dicionários.
- Assuma que poderão haver valores-chave em comum entre os dicionários.

Resultado esperado:
Dicionario_1                | Dicionario_2                | Saída
{"a": 10, "b": 20, "c": 30} | {"c": 35, "d": 45, "e": 55} | {"a": 10, "b": 20, "c": 35, "d": 45, "e": 55}
"""

# Entrada - Exemplo
dicionario_1 = {"a": 10, "b": 20, "c": 30}
dicionario_2 = {"c": 35, "d": 45, "e": 55}

# Opção 1
dicionario_saida = dicionario_1 | dicionario_2

print(f"Saída: {dicionario_saida}")

# Opção 2
dicionario_saida = dicionario_1.copy()
dicionario_saida.update(dicionario_2)

print(f"Saída: {dicionario_saida}")

# Opção 3
dicionario_saida = {**dicionario_1, **dicionario_2}

print(f"Saída: {dicionario_saida}")

