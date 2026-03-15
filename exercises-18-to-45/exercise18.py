# 18. Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0
b: int = 0
c: int = 0

# INICIO
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
if (a < b):
    c = b - a
elif (a > b):
    c = a - b
print(f"A diferença entre os dois números (maior pelo menor) é {c}")
# FIM
