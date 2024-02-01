# > Exercício 030

"""
Descrição:
- Escreva um programa Python que imprima o segundo menor valor de uma lista.
- Assuma que a lista pode ter elementos repetidos.
- Se a lista estiver vazia ou tiver apenas um elemento, imprima a mensagem "Lista vazia".

Resultado esperado:
Entrada       | Saída
[-1, -2, -3]  | -2
[0, 1, 2, 1]  | 1
[-1, -2]      | -2
[10]          | Lista vazia
[]            | Lista vazia
"""

# Entrada - Exemplo
lista_entrada = [1, 3, 2, 2, 3, 4, 4, 2, 1]

#Opção 1
if len(lista_entrada) > 1:
    lista_ordenada = sorted(set(lista_entrada))    
    print(f"Saída: {lista_ordenada[1]}")
else:
      print(f"Saída: Lista Vazia")
       
#Opção 2
if len(lista_entrada) > 1:
    sem_duplicados = set(lista_entrada)
    sem_duplicados.remove(min(sem_duplicados))
    print(f"Saída: {min(sem_duplicados)}")
else:
      print(f"Saída: Lista Vazia")



