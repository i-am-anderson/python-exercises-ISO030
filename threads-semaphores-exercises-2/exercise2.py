# 2. 4 cavaleiros caminham por um corredor, simultaneamente, de 2 a 4 m por 50 ms. O corredor é escuro, tem 2 km e em 500 m, há uma única tocha. O cavaleiro que pegar a tocha, aumenta sua velocidade, somando mais 2 m por 50 ms ao valor que já fazia. Em 1,5 km, existe uma pedra brilhante. O cavaleiro que pegar a pedra, aumenta sua velocidade, somando mais 2 m por 50 ms ao valor que já fazia (O cavaleiro que já detém a tocha não poderá pegar a pedra). Ao final dos 2 km, os cavaleiros se deparam com 4 portas e, um por vez pega uma porta aleatória (que não pode repetir) e entra nela. Apenas uma porta leva à saída. As outras 3 tem monstros que os devoram.

import multiprocessing
import time
import random

good_door: int = 0
doors: None
stone_knight: None
torch_knight: None
sem: None


def init(val1, val2, val3, val4, s):
    global doors, good_door, stone_knight, torch_knight, sem
    doors = val1
    stone_knight = val2
    torch_knight = val3
    good_door = val4
    sem = s


def process_thread(id):
    global doors, good_door, stone_knight, torch_knight, sem

    torch_checked: bool = False
    stone_checked: bool = False
    distance: int = 0
    speed: int = 0
    total_distance: int = 2000
    first_checkpoint: int = 500
    second_checkpoint: int = 1500

    print(f"Cavaleiro \033[94m[{id}]\033[0m começou a caminhar.")

    while distance < total_distance:
        # Velocidade entre 2 e 4 m por 50 ms
        speed = random.randint(2, 4)

        if torch_knight.value == id:
            speed += 2

        if stone_knight.value == id:
            speed += 2

        distance += speed  # Atualiza a distância percorrida

        if distance > total_distance:
            distance = total_distance

        if torch_knight.value == id:
            print(
                f"\033[92mCavaleiro [{id}] [COM TOCHA] está caminhando com velocidade de [{speed}]. Distância percorrida: [{distance}] metros.\033[0m"
            )
        elif stone_knight.value == id:
            print(
                f"\033[93mCavaleiro [{id}] [COM PEDRA] está caminhando com velocidade de [{speed}]. Distância percorrida: [{distance}] metros.\033[0m"
            )
        else:
            print(
                f"Cavaleiro \033[94m[{id}]\033[0m está caminhando com velocidade de \033[94m[{speed}]\033[0m. Distância percorrida: \033[94m[{distance}]\033[0m metros."
            )

        time.sleep(0.05)

        if distance >= first_checkpoint and not torch_checked:
            with sem:
                if torch_knight.value == -1:
                    torch_knight.value = id
                    torch_checked = True
                    print(
                        f"\033[92mCavaleiro \033[94m[{id}]\033[0m pegou a tocha! Velocidade aumentada.\033[0m"
                    )

        if distance >= second_checkpoint and not stone_checked:
            with sem:
                if stone_knight.value == -1 and torch_knight.value != id:
                    stone_knight.value = id
                    stone_checked = True
                    print(
                        f"\033[93mCavaleiro [{id}] pegou a pedra! Velocidade aumentada.\033[0m"
                    )

    with sem:
        print(f"\n\033[93m>>> Cavaleiro [{id}] chegou às portas. <<<\033[0m\n")
        # verifica quantas portas tem disponivel
        available_doors = len(doors)

        # escolhe uma porta aleatória
        chose_door = random.randint(0, available_doors - 1)

        print(
            f"\033[93mCavaleiro [{id}] escolheu a porta [{doors[chose_door]}]\033[0m.\n"
        )

        if doors[chose_door] == good_door.value:
            print(f"\033[92mCavaleiro [{id}] encontrou a saída! SUCESSO!\033[0m\n")
        else:
            print(
                f"\033[91mCavaleiro [{id}] foi devorado por um monstro! GAME OVER.\033[0m\n"
            )

        # retira a porta escolhida da lista de portas disponíveis
        doors.pop(chose_door)


def main():
    threads: int = 4
    params: int = [0] * threads
    stone: int = 0
    torch: int = 0
    good_door: int = 0
    semaphore = None

    with multiprocessing.Manager() as manager:
        # Variáveis compartilhadas para controlar o acesso às portas, pedra e tocha
        doors = manager.list([1, 2, 3, 4])  # Lista de portas disponíveis
        stone = manager.Value("i", -1)  # -1 indica que a pedra ainda não foi pega
        torch = manager.Value("i", -1)  # -1 indica que a tocha ainda não foi pega
        good_door = manager.Value("i", 0)  # Valor da porta correta

        # Semáforo controla a escolha da porta: 1 por vez
        semaphore = manager.Semaphore(1)

        good_door.value = random.randint(1, 4)

        for i in range(threads):
            params[i] = i + 1

        with multiprocessing.Pool(
            processes=threads,
            initializer=init,
            initargs=(doors, stone, torch, good_door, semaphore),
        ) as pool:
            pool.map(process_thread, params)


if __name__ == "__main__":
    main()
