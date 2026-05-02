import platform
import subprocess


def check_os():
    so: str = ""
    so = platform.system()
    return so


def list_processes():
    command: str = ""
    vector_command: str = []
    output: str = ""
    line: str = ""

    if check_os() == "Linux":
        command = "ps -ef"
        vector_command = command.split()
        output = subprocess.Popen(vector_command, stdout=subprocess.PIPE)
        line = output.stdout.readline().decode("utf-8", errors="ignore")

        while line:
            print(line.strip())
            line = output.stdout.readline().decode("utf-8", errors="ignore")
    elif check_os() == "Windows":
        command = "TASKLIST /FO TABLE"
        vector_command = command.split()
        output = subprocess.Popen(vector_command, stdout=subprocess.PIPE)
        line = output.stdout.readline().decode("utf-8", errors="ignore")

        while line:
            print(line.strip())
            line = output.stdout.readline().decode("utf-8", errors="ignore")
    else:
        print("Sistema operacional não suportado.")

    input("\nPressione Enter para continuar...")


def kill_process_by_pid():
    pid: int = 0
    command: str = ""
    vector_command: str = []

    if check_os() == "Linux":
        pid = int(input("Digite o PID do processo que deseja matar: "))
        command = f"kill -9 {pid}"
        vector_command = command.split()
        subprocess.run(vector_command)
    elif check_os() == "Windows":
        pid = int(input("Digite o PID do processo que deseja matar: "))
        command = f"TASKKILL /PID {pid}"
        vector_command = command.split()
        subprocess.run(vector_command)
    else:
        print("Sistema operacional não suportado.")


def kill_process_by_name():
    name: str = ""
    command: str = ""
    vector_command: str = []

    if check_os() == "Linux":
        name = input("Digite o nome do processo que deseja matar: ")
        command = f"pkill -f {name}"
        vector_command = command.split()
        subprocess.run(vector_command)
    elif check_os() == "Windows":
        name = input("Digite o nome do processo que deseja matar: ")
        command = f"TASKKILL /IM {name}"
        vector_command = command.split()
        subprocess.run(vector_command)
    else:
        print("Sistema operacional não suportado.")


def menu():
    choice: int = 0

    subprocess.run("clear" if check_os() == "Linux" else "cls", shell=True)
    print("\nEscolha uma opção:")
    print("1 - Listar processos")
    print("2 - Matar processo por PID")
    print("3 - Matar processo por nome")
    print("4 - Encerrar a aplicação")

    choice = int(input("Digite sua escolha: "))

    if choice < 1 or choice > 4:
        print("Opção inválida. Tente novamente.")
        return menu()

    if choice == 1:
        list_processes()
    elif choice == 2:
        kill_process_by_pid()
    elif choice == 3:
        kill_process_by_name()
    elif choice == 4:
        print("Encerrando a aplicação...")
        exit(0)


def main():
    while True:
        menu()


if __name__ == "__main__":
    main()
