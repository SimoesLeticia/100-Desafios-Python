# > Exercício 020

"""
Descrição:
- Escreva um programa Python que verifique se uma lista está vazia ou não.
- Se a lista estiver vazia, imprima a mensagem "Lista está vazia". Caso contrário, imprima a mensagem "Lista não está vazia".

Resultado esperado:
Entrada  | Saída
[]       | Lista está vazia
[0]      | Lista não está vazia
[1, 2 3] | Lista não está vazia
"""

# Entrada - Exemplo
lista_entrada = []

# Opção 1
if len(lista_entrada) == 0:
    print("Saída: Lista está vazia")
else:
    print("Saída: Lista não está vazia")

# Opção 2
if not lista_entrada:
    print("Saída: Lista está vazia")
else:
    print("Saída: Lista não está vazia")

