# 23. Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0
b: int = 0
c: int = 0
d: int = 0

# INICIO
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))
d = int(input("Digite um valor para D: "))
if (a < b and b < c and d != a and d != b and d != c):
    if (d > c):
        print(f"Em ordem crescente: {a},{b},{c},{d}")
    elif (d < c and d > b):
        print(f"Em ordem crescente: {a},{b},{d},{c}")
    elif (d < b and d > a):
        print(f"Em ordem crescente: {a},{d},{b},{c}")
    else:
        print(f"Em ordem crescente: {d},{a},{b},{c}")
else:
    print("Os valores precisam ser diferentes e A, B, C precisam estar em ordem crescente!")
# FIM
