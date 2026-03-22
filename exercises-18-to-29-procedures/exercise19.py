# 19. Receba 2 valores reais. Calcule e mostre o maior deles.

# DECLARAÇÃO DE VARIÁVEIS
a: float = 0.0
b: float = 0.0


def calc():
    global a
    global b
    if (a < b):
        print(f"B > A, logo B = {b:,.2f}")
    elif (a > b):
        print(f"A > B, logo A = {a:,.2f}")
    else:
        print("Os números são iguais!")


def main():
    global a
    global b
    # INICIO
    a = float(input("Digite um número para A: "))
    b = float(input("Digite um número para B: "))
    calc()
    # FIM


if __name__ == "__main__":
    main()
