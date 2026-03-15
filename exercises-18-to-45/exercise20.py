# 20. Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

# DECLARAÇÃO DE VARIÁVEIS
a: float = 0.0
b: float = 0.0
c: float = 0.0
delta: float = 0.0
x1: float = 0.0
x2: float = 0.0

# INICIO
a = float(input("Digite um número para o coeficiente A: "))
b = float(input("Digite um número para o coeficiente B: "))
c = float(input("Digite um número para o coeficiente C: "))
delta = b ** 2 - 4 * a * c
if (a != 0 and delta >= 0):
    if (delta > 0):
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"As raízes reais da equação são x'={x1:,.2f} e x''={x2:,.2f}")
    else:
        x1 = x2 = -b / (2 * a)
        print(f"A equação tem apenas UMA raíz x={x1:,.2f}")
else:
    print("Não há raízes reais para esses coeficientes!")
# FIM
