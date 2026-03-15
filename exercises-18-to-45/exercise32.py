# 32. Receba um número inteiro. Calcule e mostre o seu fatorial.

# DECLARAÇÃO DE VARIÁVEIS
num: int = 0
fact: int = 1

# INICIO
while (num <= 0):
    num = int(input("Digite um número inteiro: "))
for n in range(num, 0, -1):
    fact *= n
print(fact)
# FIM
