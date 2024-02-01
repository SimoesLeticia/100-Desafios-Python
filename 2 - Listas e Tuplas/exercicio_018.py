# > Exercício 018

"""
Descrição:
- Escreva um programa Python que imprima os elementos de uma lista na mesma linha.
- Os elementos devem ser separados apenas por espaço (não por vírgula).
- A saída NÃO deve incluir colchetes de abertura e fechamento.

Resultado esperado:
Entrada         | Saída
[3, 4, 5, 6]    | 3 4 5 6
["a", "b", "c"] | a b c
"""

# Entrada - Exemplo
lista_entrada = ["a", "b", "c", 3, 4, 5, 6]

# Opção 1
print(*lista_entrada) # "*" é um operador de desempacotamento, cada elemento da lista se torna um argumento separado para função print

# Opção 2 
for elemento in lista_entrada:
    print(elemento, end = " ") # Passamos o parâmetro end = " " para que os elementos sejam impressos em sequência, separados por espaços.