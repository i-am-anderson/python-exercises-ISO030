# 21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#   a. Se a média for >= 6,0 exibir “APROVADO”;
#   b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
#   c. Se a média for < 3,0 exibir “RETIDO”.
import os

nome: str = ""
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ""
arq: str = ""


# Procedimento
def escreveArq(caminho, arquivo, linha_arq):
    file: str = ""
    tipo: str = ""
    enc: str = ""

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = "w"
        enc = "utf-8"
        file = os.path.join(dir, arq)

        if (os.path.exists(file) and os.path.isfile(file)):
            tipo = "a"

        with open(file, tipo, encoding=enc) as fl:
            fl.write(linha_arq)

    else:
        print("Diretório não existe!")

# Procedimento


def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir
    global arq

    linha: str = ""
    dir = "/tmp/exercicios"
    arq = "ex21.txt"

    linha = nm + "; " + str(nt1) + "; " + str(nt2) + "; " + \
        str(nt3) + "; " + str(nt4) + "; " + str(vlr_med) + "\n"

    escreveArq(dir, arq, linha)


# Função
def med(n1, n2, n3, n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media


# Procedimento
def entrada():
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    nome = input("Digite o nome: ")
    nota1 = float(input("Digita a nota 1: "))
    nota2 = float(input("Digita a nota 2: "))
    nota3 = float(input("Digita a nota 3: "))
    nota4 = float(input("Digita a nota 4: "))

    valor_media = med(nota1, nota2, nota3, nota4)

    print(f"Valor da média: {valor_media}")

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)


def main():
    contador: int = 0

    os.makedirs("/tmp/exercicios", exist_ok=True)
    os.chmod("/tmp/exercicios", 0o744)

    while (contador < 5):
        entrada()
        contador += 1


if __name__ == "__main__":
    main()
