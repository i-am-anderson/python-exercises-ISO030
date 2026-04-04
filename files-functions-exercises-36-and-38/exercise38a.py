# 38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.
import os

dir: str = ""
arq: str = ""


# Procedimento
def grava(cont, rslt):
    global dir
    global arq

    dir = "/tmp/exercicios"
    arq = "ex38a.txt"

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


def main():
    count: int = 0
    num: float = 0
    bigger: int = 0
    smaller: int = 0
    phrase: str = ""

    # cria o diretório e dá as permissões necessárias
    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    while count < 100:
        num = float(input(f"Digite o {count + 1}° número: "))
        if num > 0:
            if count == 0:
                bigger = smaller = num
            else:
                if num > bigger:
                    bigger = num
                elif num < smaller:
                    smaller = num
            grava(count, num)
            count += 1

    phrase = f"\nMaior = {bigger}\nMenor = {smaller}\n"

    grava(-1, phrase)

    print(
        f"\nO menor valor digitado foi: {smaller}\nO maior valor digitado foi: {bigger}"
    )


if __name__ == "__main__":
    main()
