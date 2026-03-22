# 26. Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0
b: int = 0


def multiple():
    global a
    global b
    if (a >= b and a % b == 0):
        print(f"A = {a} é múltiplo de B = {b}")
    elif (a < b and b % a == 0):
        print(f"B = {b} é múltiplo de A = {a}")
    else:
        print(f"A = {a} e B = {b} não são multiplos!")


def main():
    global a
    global b
    # INICIO
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    multiple()
    # FIM


if __name__ == "__main__":
    main()
