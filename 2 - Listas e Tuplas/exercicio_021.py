# > Exercício 021

"""
Descrição:
- Escreva um programa Python que imprima os elementos de uma lista seguidos de seus índices correspondentes.
- Cada elemento e seu índice devem estar na mesma linha separados por um espaço.
- Se a lista estiver vazia, imprima a mensagem "Lista vazia".

Resultado esperado:
Entrada         | Saída
[1, 2, 3, 4]    | 1 0
                | 2 1
                | 3 2
                | 4 3
["A", "B", "C"] | A 0
                | B 1
                | C 2
[]              | Lista vazia
"""

# Entrada - Exemplo
lista_entrada = ["A", "B", "C"]

# Opção 1
if not lista_entrada:
    print("Saída: Lista vazia")
else:
    for I in range(len(lista_entrada)):
        print(f"Saída: {lista_entrada[I]} {I}")

# Opção 2
if not lista_entrada:
    print("Saída: Lista vazia")
else:
    for I, elemento in enumerate(lista_entrada):
        print(f"Saída: {elemento} {I}")