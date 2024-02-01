# > Exercício 023

"""
Descrição:
- Escreva um programa Python que remova elementos duplicados de uma lista, mantendo apenas uma ocorrência de cada elemento da lista.
- O programa deverá imprimir a versão final da lista.

Resultado esperado:
Entrada               | Saída
["A", "A", "B", "A"]  | ["A", "B"]
[1, 1, 2, 3, 4, 4, 5] | [1, 2, 3, 4, 5]
[10, 11, 12, 13]      | [10, 11, 12, 13]
[]                    | []
"""

# Entrada - Exemplo
lista_entrada = ["A", "A", "B", "A", "C", "D", "C"]

# Opção 1
lista_sem_duplicados = list(set(lista_entrada)) # set() pode ser utilizado para remover registros duplicados, porém não preserva a posição inicial dos elementos na lista

print(f"Saída: {lista_sem_duplicados}")

# Opção 2
conjunto_elementos   = set()
lista_sem_duplicados = []

for elemento in lista_entrada:
    if elemento not in conjunto_elementos:
        conjunto_elementos.add(elemento)
        lista_sem_duplicados.append(elemento) # Essa opção utiliza set(), porém preserva a posição inicial dos elementos na lista

print(f"Saída: {lista_sem_duplicados}")        

# Opção 3
lista_sem_duplicados = list(dict.fromkeys(lista_entrada)) # Essa opção cria um dicionário com os elementos da lista sem duplicá-los e preserva a posição inicial dos elementos

print(f"Saída: {lista_sem_duplicados}")

