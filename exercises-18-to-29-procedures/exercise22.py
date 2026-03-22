# 22. Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0
b: int = 0


def sort():
    global a
    global b
    if (a != b):
        if (a < b):
            print(f"Em ordem crescente: {a},{b}")
        else:
            print(f"Em ordem crescente: {b},{a}")
    else:
        print("Os valores precisam ser diferentes!")


def main():
    global a
    global b
    # INICIO
    a = int(input("Insira o primeiro valor: "))
    b = int(input("Insira o segundo valor: "))
    sort()
    # FIM


if __name__ == "__main__":
    main()
