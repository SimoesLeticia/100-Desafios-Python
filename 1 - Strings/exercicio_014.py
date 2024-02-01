# > Exercício 014

"""
Descrição:
- Escreva um programa Python que inverta as palavras individuais da string s e altere sua capitalização. Isso é, letras maiúsculas devem ser trocadas para minúsculas e vice-versa.
- Assuma que a string contenha apenas letras.
- Assum auqe espaços sejam usados para separar as palavras.

Resultado esperado:
Entrada           | Saída
Olá Mundo         | ÁLo ODNUm
Python é Incrível | NOHTYp É LEVÍRCNi
Python            | NOHTYp
"""

# Entrada - Exemplo
s = "Python é Incrível"

# Opção 1
saida = ""

lista_palavras = s.split(" ") #Armazena strings individualmente numa lista. Ex.: ["Olá", "Mundo"]

for palavra in lista_palavras:
    string_invertida = palavra[::-1] # Também poderia ser usado "".join(reversed(palavra))    
    string_capitalizada = string_invertida.swapcase() # swapcase = método que inverte maiúsculas para minúsculas e vice-versa 
    saida += string_capitalizada + " "
    
saida.rstrip() # remove o espaço no final da string

print(f"Saída: {saida}")

# Opção 2
lista_palavras_invertidas = []

lista_palavras = s.split(" ")

for palavra in lista_palavras:
    string_invertida = palavra[::-1] 
    string_capitalizada = string_invertida.swapcase()  
    lista_palavras_invertidas.append(string_capitalizada) # Armazena as palavras invertidas numa nova lista

saida = " ".join(lista_palavras_invertidas) # Reune as palavras de volta numa única string

print(f"Saída: {saida}")