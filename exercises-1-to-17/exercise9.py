# 9. Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0
b: int = 0
c: int = 0

# INICIO
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = a ** 2 + b ** 2
print(f"A soma dos quadrados de {a} e {b} é {c}")
# FIM
