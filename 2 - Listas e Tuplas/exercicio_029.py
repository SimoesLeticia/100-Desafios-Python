# > Exercício 029

"""
Descrição:
- Escreva um programa Python que imprima o segundo maior valor de uma lista.
- Assuma que a lista pode ter elementos repetidos.
- Se a lista estiver vazia ou tiver apenas um elemento, imprima a mensagem "Lista vazia".

Resultado esperado:
Entrada       | Saída
[5, 1, 8, -1] | 5
[1, 2, 2]     | 1
[-1, -2]      | -2
[10]          | Lista vazia
[]            | Lista vazia
"""

# Entrada - Exemplo
lista_entrada = [1, 3, 2, 2, 3, 4, 4, 2, 1] 

if len(lista_entrada) > 1:
    sem_duplicados = set(lista_entrada)
    sem_duplicados.remove(max(sem_duplicados))
    print(f"Saída: {max(sem_duplicados)}")
else:
      print(f"Saída: Lista Vazia")