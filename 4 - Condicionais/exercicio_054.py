# > Exercício 054

"""
Descrição:
- Escreva um programa em Python que imprima as soluções positivas e negativas (raízes) para uma equação quadrática.
    - Se a equação tiver apenas uma solução, o programa deverá imprimir essa solução.
    - Se tiver duas soluções, o programa deverá imprimir a negativa primeiro e a positiva em seguida na mesma linha.
    - Se a equação não tiver soluções reais, o programa deverá imprimir "Raízes Complexas".

- Para determinar o número de soluções, utilize a fórmula de delta: Δ = b² - 4ac
    - Se o resultado de delta for negativo, a equação não tem soluções reais (apenas raízes complexas).
    - Se o resultado de delta for 0, há apenas uma solução.
    - Se o resultado de delta for positivo, há duas soluções reais.

- Uma equação quadrática tem a seguinte fórmula: ax² + bx + c = 0
    - Por exemplo: x² + 2x + 1 = 0

- Para resolver essa equação, usamos a fórmula quadrática: x = (-b ± √(b² - 4ac)) / (2a)
- Encontramos o resultado substituindo os valores de a, b e c na fórmula.

Resultado esperado:
Entrada  | Saída
1, 2, 1  | -1.0
2, 5, -3 | -3 0.5
3, 4, 5  | Raízes Complexas
"""

# Bibliotecas
import math

# Entrada - Exemplo
entrada = "1, -5, 6"

a, b, c = map(float, entrada.split(','))

# Opção 1
delta = b**2 - 4*a*c

if delta < 0:
    print("Raízes Complexas")
elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2*a)
    print(x)
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"{x1} {x2}")