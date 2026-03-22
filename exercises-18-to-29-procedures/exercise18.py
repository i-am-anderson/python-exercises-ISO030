# 18. Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

# DECLARAÇÃO DE VARIÁVEIS
a: int = 0
b: int = 0


def diference():
    global a
    global b
    c: int = 0
    if (a < b):
        c = b - a
    elif (a > b):
        c = a - b
    print(f"A diferença entre os dois números (maior pelo menor) é {c}")


def main():
    global a
    global b
    # INICIO
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    diference()
    # FIM


if __name__ == "__main__":
    main()
