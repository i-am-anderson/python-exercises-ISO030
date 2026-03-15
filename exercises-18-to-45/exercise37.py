# 37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

# DECLARAÇÃO DE VARIÁVEIS
x: int = 0
y: int = 1
curr: int = 0
n: int = 0

# INICIO
while (n <= 0):
    n = int(input("Digite um número inteiro: "))

for _ in range(n):
    if (x == 0):
        x = 1
    else:
        y = curr
        curr = x + y
        x = y

    print(curr, end=", ")
# FIM
