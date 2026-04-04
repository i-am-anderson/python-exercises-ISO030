# 36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
import os

dir: str = ""
arq: str = ""


# Procedimento de gravação em arquivo
def grava(cont, rslt):
    global dir
    global arq

    dir = "/tmp/exercicios"
    arq = "ex36.txt"

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    if os.path.exists(dir) and os.path.isdir(dir):
        tipo = "w"
        enc = "utf-8"
        linha = str(rslt) + "\n"
        file = os.path.join(dir, arq)

        if os.path.exists(file) and os.path.isfile(file) and (cont > 0 or cont == -1):
            tipo = "a"

        with open(file, tipo, encoding=enc) as fl:
            fl.write(linha)
    else:
        print("Diretório não existe!")


# Função que calcula o fatorial
def calc_fact(i):
    fact: int = 1

    for f in range(1, i + 1, 1):
        fact *= f

    return fact


# Função que calcula a divisão
def calc_div(i):
    div: float = 0.0
    div = 1 / calc_fact(i)
    return div


# Função que faz o somatório e imprime em tela
def calc_sum(n):
    term: float = 0.0
    sum_: float = 0.0

    for i in range(0, n + 1, 1):
        term = calc_div(i)
        sum_ += term

        grava(i, term)

        print(f"{term:.2f}", end="")

        if i < n:
            print(" + ", end="")
        else:
            print(" = ", end="")

    grava(-1, f"\nResultado: {sum_}")

    return sum_


def main():
    result_fact: int = 0
    n: int = 0

    # cria o diretório e dá as permissões necessárias
    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    while n <= 0:
        n = int(input("Digite um número: "))

    result_fact = calc_sum(n)

    print(f"{result_fact:,.2f}")


if __name__ == "__main__":
    main()
