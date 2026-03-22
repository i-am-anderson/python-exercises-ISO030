# 25. Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

# DECLARAÇÃO DE VARIÁVEIS
h_start: int = 0
m_start: int = 0
h_final: int = 0
m_final: int = 0


def calcTime():
    global h_start
    global m_start
    global h_final
    global m_final
    start: int = 0
    final: int = 0
    dur: int = 0
    start = (h_start * 60) + m_start
    final = (h_final * 60) + m_final
    if (start < final):
        dur = final - start
    else:
        dur = (1440 - start) + final
    print(f"Duração do jogo - {dur // 60}:{dur % 60}")


def main():
    global h_start
    global m_start
    global h_final
    global m_final
    # INICIO
    h_start = int(input("Hora inicial: "))
    m_start = int(input("Minuto inicial: "))
    h_final = int(input("Hora final: "))
    m_final = int(input("Minuto final: "))
    calcTime()
    # FIM


if __name__ == "__main__":
    main()
