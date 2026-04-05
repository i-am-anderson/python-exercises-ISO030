# 30. Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a idade em anos, meses e dias, considerando os anos bissextos.


def main():
    dia_nasc: int = 0
    mes_nasc: int = 0
    ano_nasc: int = 0
    dia_atual: int = 0
    mes_atual: int = 0
    ano_atual: int = 0
    dia: int = 0
    mes: int = 0
    ano: int = 0
    mes_anterior: int = 0
    ano_mes_anterior: int = 0
    qtd_dias_mes: int = 0

    dia_nasc = int(input("Digite o dia do nascimento: "))
    mes_nasc = int(input("Digite o mês do nascimento: "))
    ano_nasc = int(input("Digite o ano do nascimento: "))
    dia_atual = int(input("Digite o dia atual: "))
    mes_atual = int(input("Digite o mês atual: "))
    ano_atual = int(input("Digite o ano atual: "))

    ano = ano_atual - ano_nasc

    if mes_atual >= mes_nasc:
        mes = mes_atual - mes_nasc
    else:
        ano -= 1
        mes = 12 + (mes_atual - mes_nasc)

    if dia_atual >= dia_nasc:
        dia = dia_atual - dia_nasc
        print(f"Idade: {ano} anos, {mes} meses e {dia} dias.")
    else:
        mes -= 1
        if mes < 0:
            mes = 11
            ano -= 1
        mes_anterior = mes_atual - 1
        ano_mes_anterior = ano_atual

        if mes_anterior == 0:
            mes_anterior = 12
            ano_mes_anterior -= 1

        if mes_anterior in [4, 6, 9, 11]:
            qtd_dias_mes = 30
        elif mes_anterior == 2:
            if (ano_mes_anterior % 4 == 0 and ano_mes_anterior % 100 != 0) or (
                ano_mes_anterior % 400 == 0
            ):
                qtd_dias_mes = 29
            else:
                qtd_dias_mes = 28
        else:
            qtd_dias_mes = 31

        dia = dia_atual + (qtd_dias_mes - dia_nasc)

        print(f"Idade: {ano} anos, {mes} meses e {dia} dias.")


if __name__ == "__main__":
    main()
