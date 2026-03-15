# 35. Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

# DECLARAÇÃO DE VARIÁVEIS
x: int = 0
y: int = 0
greater: int = 0
lower: int = 0
sm: int = 0

# INICIO
while (x == y):
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
if (x > y):
    greater = x
    lower = y
else:
    greater = y
    lower = x
for i in range(lower + 1, greater, 1):
    if (i % 2 != 0):
        sm += i

print(f"O número {greater} é o maior dos dois!")
print(f"A soma dos números ímpares entre {lower} e {greater} é: {sm}")
# FIM
