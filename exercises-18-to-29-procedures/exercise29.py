# 29. Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

# DECLARAÇÃO DE VARIÁVEIS
tipo: int = 0
valor: float = 0.0


def calc(t, v):
    # considerando que 3% a.m. e 5% a.m.
    if (t == 1):
        v = 1.03 * v
    else:
        v = 1.05 * v
    print(f"O valor corrgido em 30 dias será  de R$ {v:,.2f}")


def main():
    global tipo
    global valor
    # INICIO
    while (tipo <= 0 or tipo > 2):
        tipo = int(input("Digite a operaçao: (1 = poupança e 2 = renda fixa): "))
        valor = float(input("Digite o valor: R$ "))
    calc(tipo, valor)
    # FIM


if __name__ == "__main__":
    main()
