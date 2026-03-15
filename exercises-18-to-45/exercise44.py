# 44. Receba o número da base e do expoente. Calcule e mostre o valor da potência.

# DECLARAÇÃO DE VARIÁVEIS
base: int = 0
exp: int = 0
pot: int = 1

# INICIO
base = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))
for _ in range(exp):
    pot *= base
print(f"{base}^{exp} = {pot}")
# FIM
