# 5. Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).

# DECLARAÇÃO DE VARIÁVEIS
a: float = 0.0
b: float = 0.0
c: float = 0.0
delta: float = 0.0
x1: float = 0.0
x2: float = 0.0

# INICIO
a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))
delta = (b ** 2 - 4 * a * c)
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)
print(f"As raízes reais da equação são x'={x1:,.2f} e x''={x2:,.2f}")
# FIM
