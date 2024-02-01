# > Exercício 027

"""
Descrição:
- Escreva um programa Python que calcule a distância entre dois pontos 3D.
- Os pontos são representados por duas listas com três elementos. O primeiro elemento é a coordenada x. O segundo elemento é a coordenada y. O terceiro elemento é a coordenada z.

Fórmula para encontrar a distância:
AB = √(x₁ - x₂)² + (y₁ - y₂)² + (z₁ - z₂)²

Onde:
A(x₁, y₁, z₁) e B(x₂, y₂, z₂)

Resultado esperado:
Ponto_A      | Ponto_B    | Saída
[1, 2, 3]    | [1, 2, 3]  | 0
[3, 4, 5]    | [1, 3, 5]  | 2.23607
[-3, -4, -5] | [2, 0, -4] | 6.48074
"""

# Entrada - Exemplo
ponto_a = [-3, -4, -5]
ponto_b = [2, 0, -4] 

# Opção 1
soma = ((ponto_a[0] - ponto_b[0])**2 + (ponto_a[1] - ponto_b[1])**2 + (ponto_a[2] - ponto_b[2])**2) # **2 representa a pontencia (²)

distancia = soma ** (1/2) # (1/2) representa a raiz (√)

print(f"Saída: {distancia}")

# Opção 2
import math

soma = ((ponto_a[0] - ponto_b[0])**2 + (ponto_a[1] - ponto_b[1])**2 + (ponto_a[2] - ponto_b[2])**2)

distancia = math.sqrt(soma) # sqrt é um método da biblioteca math que retorna a raiz quadrada de um número

print(f"Saída: {distancia}")

# Opção 3
x1, y1, z1 = ponto_a
x2, y2, z2 = ponto_b

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

print(f"Saída: {distancia}")