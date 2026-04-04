# 34. Receba um número. Calcule e mostre os resultados da tabuada desse número.
import os

valor: int = 0
dir: str = ""
arq: str = ""


# Função
def mult(vlr, tab):
    res: int = 0
    res = vlr * tab
    return res


# Procedimento
def grava(c, rslt):
    global dir
    global arq

    dir = "/tmp/exercicios"
    arq = "ex34.txt"

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    if os.path.exists(dir) and os.path.isdir(dir):
        tipo = "w"
        enc = "utf-8"
        linha = str(rslt) + "\n"
        file = os.path.join(dir, arq)

        if os.path.exists(file) and os.path.isfile(file) and c > 0:
            tipo = "a"

        with open(file, tipo, encoding=enc) as fl:
            fl.write(linha)
    else:
        print("Diretório não existe!")


def main():
    global valor
    contador: int = 0
    result: int = 0

    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    valor = int(input("Insira um valor entre 1 e 10: "))

    while contador <= 10:
        result = mult(valor, contador)
        grava(contador, result)
        contador += 1


if __name__ == "__main__":
    main()
