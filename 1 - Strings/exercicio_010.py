# > Exercício 010

"""
Descrição:
- Escreva um programa Python que verifique se a string s é um pangrama, isso é, contém todas as letras do alfabeto.
- Se a string contém todas as letras do alfabeto, o programa deverá imprimir "True". Caso contrário, o programa deverá imprimir "False".
- Antes de comparar os caracteres, você deve converter a string para minúscula.
- Se a string contiver espaços, ignore-os antes de encontrar o resultado.
- Assuma que a string não contém nenhum outro símbolo, apenas espaços (possivelmente).
- Considere estas letras como parte do alfabeto: "abcdefghijklmnopqrstuvwxyz".

Resultado esperado:
Entrada                                                                                                           | Saída
O rato roeu a roupa do rei de Roma                                                                                | False
aáãâàbcçdeéêèfghiíîìjklmnoóôòõpqrstuúûùüvwxyz                                                                     | True
abcdefghijklmnopqrstuvwxyz                                                                                        | True*
The quick brown fox jumps over the lazy dog                                                                       | True*
TV faz quengo explodir com whisky JB                                                                              | True*
À noite vovô Kowalsky vê o ímã cair no pé do pingüim queixoso e vovó põe açúcar no chá de tâmaras do jabuti feliz | True

*Na # Opção 2 retornará False, pois consideramos letras com acentos gráficos e sinais diacríticos.
"""

# Entrada - Exemplo
s = "À noite vovô Kowalsky vê o ímã cair no pé do pingüim queixoso e vovó põe açúcar no chá de tâmaras do jabuti feliz"

# Opção 1
import string

# Remoção dos espaços e conversão para minúsculas
s_minusculas_sem_espacos = s.replace(" ", "").lower()

pangrama = True

for char in string.ascii_lowercase: #Constante da biblioteca string, contém a string 'abcdefghijklmnopqrstuvwxyz'
    if char not in s_minusculas_sem_espacos:
        pangrama = False
        break

print(f"Saída: {pangrama}")

# Opção 2
# Nessa versão consideramos letras com acentos gráficos e sinais diacríticos.

alfabeto = "aáãâàbcçdeéêfghiíjklmnoóôõpqrstuúüvwxyz"

s_minusculas_sem_espacos = s.replace(" ", "").lower()

pangrama = True

for char in alfabeto:
    if char not in s_minusculas_sem_espacos:
        pangrama = False
        break

print(f"Saída: {pangrama}")