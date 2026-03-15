# 19. Receba 2 valores reais. Calcule e mostre o maior deles.

# DECLARAÇÃO DE VARIÁVEIS
a: float = 0.0
b: float = 0.0

# INICIO
a = float(input("Digite um número para A: "))
b = float(input("Digite um número para B: "))
if (a < b):
    print(f"B > A, logo B = {b:,.2f}")
elif (a > b):
    print(f"A > B, logo A = {a:,.2f}")
else:
    print("Os números são iguais!")
# FIM
