# > Exercício 057

"""
Descrição:
- Escreva um programa Python que simule o jogo Pedra, Papel, Tesoura.
- O programa deve interagir com o usuário solicitando uma opção: PEDRA, PAPEL ou TESOURA.
- O usuário deverá jogar contra o programa, que escolherá uma opção aleatória.
- A escolha do programa será comparada com a escolha do usuário para determinar quem ganhará.
- O programa deverá exibir uma mensagem indicando se o usuário ganhou, perdeu ou se o jogo terminou em empate.

- Regras básicas do jogo:
    - PAPEL   vence PEDRA.
    - PEDRA   vence TESOURA.
    - TESOURA vence PAPEL.

Resultado esperado:
Entrada:
=== Bem-vindo ao jogo ===
Escolha uma das opções: PEDRA, PAPEL ou TESOURA:

Saída:
- É um empate! Seu oponente escolheu <escolha do programa>.
- Você ganhou! Seu oponente escolheu <escolha do programa>.
- Você perdeu! Seu oponente escolheu <escolha do programa>.
- Escolha inválida! Tente novamente.
"""

# Bibliotecas
import random

escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_programa = random.choice(escolhas)

print("=== Bem-vindo ao jogo ===")
entrada = input("Escolha uma das opções: PEDRA, PAPEL ou TESOURA: ").upper()

if entrada not in escolhas:
    print("Escolha inválida! Tente novamente.")
else:
    if entrada == escolha_programa:
        print(f"É um empate! Seu oponente escolheu: {escolha_programa}.")
    elif (entrada == 'PEDRA'   and escolha_programa == 'TESOURA') or \
         (entrada == 'PAPEL'   and escolha_programa == 'PEDRA')   or \
         (entrada == 'TESOURA' and escolha_programa == 'PAPEL'):
        print(f"Você ganhou! Seu oponente escolheu: {escolha_programa}.")
    else:
        print(f"Você perdeu! Seu oponente escolheu: {escolha_programa}.")