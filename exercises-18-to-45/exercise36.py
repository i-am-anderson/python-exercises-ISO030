# 36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

# DECLARAÇÃO DE VARIÁVEIS
n: int = 0
fact: int = 0
sum_: float = 0

# INICIO
while (n <= 0):
    n = int(input("Digite um número: "))
for i in range(0, n+1, 1):
    fact = 1
    for f in range(1, i + 1, 1):
        fact *= f
    sum_ += (1 / fact)

    if (i == 0):
        print("1", end="")
    else:
        print(f"{1}/{i}!", end="")

    if (i < n):
        print(" + ", end="")
    else:
        print(" = ", end="")
print(f"{sum_:,.2f}")
# FIM
