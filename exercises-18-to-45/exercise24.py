# 24. Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0

# INICIO
a = int(input("Digite um valor inteiro: "))
if (a % 2 == 0 and a % 3 == 0):
    print(f"O número {a} é divisível por 2 e 3")
else:
    print(f"O número {a} NÃO é divisível por 2 e 3")
# FIM
