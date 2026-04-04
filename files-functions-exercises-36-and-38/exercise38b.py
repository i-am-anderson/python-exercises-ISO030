# 38.
import os

dir: str = ""
arq: str = ""
new_arq: str = ""


# Procedimento
def gravar(cont, data):
    global dir
    global new_arq

    dir = "/tmp/exercicios"
    new_arq = "ex38b.txt"

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    if os.path.exists(dir) and os.path.isdir(dir):
        tipo = "w"
        enc = "utf-8"
        linha = str(data) + "\n"
        file = os.path.join(dir, new_arq)

        if os.path.exists(file) and os.path.isfile(file) and cont > 0:
            tipo = "a"

        with open(file, tipo, encoding=enc) as fl:
            fl.write(linha)
    else:
        print("Diretório não existe!")


# Procedimento
def ler():
    global dir
    global arq

    dir = "/tmp/exercicios"
    arq = "ex38a.txt"

    file: str = ""

    if os.path.exists(dir) and os.path.isdir(dir):
        file = os.path.join(dir, arq)

        if os.path.exists(file) and os.path.isfile(file):
            tipo = "r"
            enc = "utf-8"
            with open(file, tipo, encoding=enc) as fl:
                for index, line in enumerate(fl.readlines()):
                    num_to_int: int = 0

                    # se linha não tiver as palavras "Maior" e "Menor" e se linha não for vazia...
                    if (
                        line.find("Maior") == -1
                        and line.find("Menor") == -1
                        and line.strip() != ""
                    ):
                        num_to_int = int(float(line))
                        if num_to_int % 5 == 0:
                            gravar(index, num_to_int)
        else:
            print("Arquivo não existe!")
    else:
        print("Diretório não existe!")


def main():
    # cria o diretório e dá as permissões necessárias
    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    ler()


if __name__ == "__main__":
    main()
