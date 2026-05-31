# 1. Um aeroporto tem 2 pistas (norte e sul) e, em cada pista, apenas um avião pode fazer a decolagem. O procedimento de decolagem tem 4 fases (manobrar, taxiar, decolagem e afastamento da área). A fase de manobra pode durar de 300 a 700 milissegundos A fase de taxiar, de 500 a 1000 milissegundos. A fase de decolagem, de 600 a 800 milissegundos. A fase de afastamento, de 300 a 800 milissegundos. O aeroporto reúne, por ciclo, 12 aeronaves que podem decolar pela pista norte ou pela pista sul (decisão aleatória) mas, apenas 2 aviões podem circular pela área de decolagem ao mesmo tempo. Fazer uma aplicação que resolva o problema.

import multiprocessing
import time
import random

direction_shared: None
sem: None


def init(val, s):
    global direction_shared, sem
    direction_shared = val
    sem = s


def process_thread(id):
    global direction_shared, sem
    color: str = ""

    with sem:
        north_or_south = random.choice(["NORTE", "SUL"])

        # Verica a pista escolhida, se estiver ocupada muda para a outra
        if north_or_south == "NORTE" and direction_shared[0] == 1:
            north_or_south = "SUL"
        elif north_or_south == "SUL" and direction_shared[1] == 1:
            north_or_south = "NORTE"

        # Ocupa a pista
        if north_or_south == "NORTE":
            direction_shared[0] = 1
        else:
            direction_shared[1] = 1

        color = "\033[94m" if north_or_south == "NORTE" else "\033[92m"

        # Manobrar
        print(f"Avião {id} está manobrando na pista {color}{north_or_south}\033[0m.")
        time.sleep(random.uniform(0.3, 0.7))

        # Taxiar
        print(f"Avião {id} está taxiando na pista {color}{north_or_south}\033[0m.")
        time.sleep(random.uniform(0.5, 1.0))

        # Decolagem
        print(f"Avião {id} está decolando pela pista {color}{north_or_south}\033[0m.")
        time.sleep(random.uniform(0.6, 0.8))

        # Afastamento
        print(
            f"Avião {id} está se afastando da área de decolagem pela pista {color}{north_or_south}\033[0m."
        )
        time.sleep(random.uniform(0.3, 0.8))

        # Término
        print(
            f"Avião {id} terminou a decolagem pela pista {color}{north_or_south}\033[0m."
        )

        # Libera a pista
        if north_or_south == "NORTE":
            direction_shared[0] = 0
        else:
            direction_shared[1] = 0

        # Liberação
        print(
            f"Pista {color}{north_or_south}\033[0m está livre para o próximo avião.\n"
        )


def main():
    threads: int = 12
    params: int = [0] * threads
    semaphore = None
    direction: int = []

    with multiprocessing.Manager() as manager:
        # Variável compartilhada para controlar o acesso às pistas (0 = livre, 1 = ocupada)
        direction = manager.Array("i", [0] * 2)

        # Semáforo para controlar o acesso à área de decolagem, permitindo no máximo 2 aviões ao mesmo tempo
        semaphore = manager.Semaphore(2)

        for i in range(threads):
            params[i] = i + 1

        with multiprocessing.Pool(
            processes=threads,
            initializer=init,
            initargs=(direction, semaphore),
        ) as pool:
            pool.map(process_thread, params)


if __name__ == "__main__":
    main()
