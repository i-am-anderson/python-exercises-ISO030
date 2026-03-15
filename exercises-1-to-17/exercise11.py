# 11. Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.
from math import pi

# DECLARAÇÃO DE VARIÁVEIS
r: float = 0.0
c: float = 0.0

# INICIO
r = float(input("Insira o raio da circunferência: "))
c = 2 * pi * r
print(f"O comprimento da circunferência de raio {r:,.2f} é ~ {c:,.2f}")
# FIM
