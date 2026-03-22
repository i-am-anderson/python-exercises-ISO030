# 24. Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0


def divisible():
    global a
    if (a % 2 == 0 and a % 3 == 0):
        print(f"O número {a} é divisível por 2 e 3")
    else:
        print(f"O número {a} NÃO é divisível por 2 e 3")


def main():
    global a
    # INICIO
    a = int(input("Digite um valor inteiro: "))
    divisible()
    # FIM


if __name__ == "__main__":
    main()
