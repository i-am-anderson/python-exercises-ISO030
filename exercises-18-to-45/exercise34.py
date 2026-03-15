# 34. Receba um número. Calcule e mostre os resultados da tabuada desse número.

# DECLARAÇÃO DE VARIÁVEIS
num: int = 0

# INICIO
while (num <= 0 or num > 10):
    num = int(input("Digite um número: "))
for i in range(0, 11, 1):
    print(f"{i} x {num} = {i * num}")
# FIM
