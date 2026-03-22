# 27. Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

# DECLARAÇÃO DE VARIÁVEIS
n_voltas: int = 0
e_circuito: int = 0
t_duracao: int = 0


def calc(voltas, circuito, duracao):
    ext: int = 0
    v_media: int = 0
    ext = voltas * circuito
    v_media = (ext / 1000) / (duracao / 60)
    print(f"A velocidade média é de {v_media:,.2f}km/h")


def main():
    global n_voltas
    global e_circuito
    global t_duracao
    # INICIO
    while (n_voltas <= 0 and e_circuito <= 0 and t_duracao <= 0):
        n_voltas = int(input("Digite o número de voltas: "))
        e_circuito = int(input("Digite a extensão do circuito (metros): "))
        t_duracao = int(input("Digite o tempo de duração (minutos): "))
    calc(n_voltas, e_circuito, t_duracao)
    # FIM


if __name__ == "__main__":
    main()
