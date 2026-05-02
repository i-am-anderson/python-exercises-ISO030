import platform
import subprocess


def so_name():
    so: str = ""
    so = platform.system()
    return so


def ping():
    so: str = ""
    command: str = ""
    vector_command: str = []
    so = so_name()
    output: str = ""
    line: str = ""
    data: str = ""

    if so == "Linux":
        command = "ping -4 -c 1 www.google.com.br"
        vector_command = command.split()
        output = subprocess.Popen(vector_command, stdout=subprocess.PIPE)
        line = output.stdout.readline().decode("utf-8", errors="ignore")

        while line:
            if "min/avg/max/mdev" in line:
                data = line.split()
                data = data[3].split("/")
                data = data[1] + "ms"
                print(data)
            line = output.stdout.readline().decode("utf-8", errors="ignore")

    elif so == "Windows":
        command = "ping -4 -n 10 www.google.com.br"
        vector_command = command.split()
        output = subprocess.Popen(vector_command, stdout=subprocess.PIPE)
        line = output.stdout.readline().decode("utf-8", errors="ignore")

        while line:
            if "Média" in line:
                data = line.split("=")
                data = data[5]
                print(data)
            line = output.stdout.readline().decode("utf-8", errors="ignore")
    else:
        print("Sistema operacional não suportado.")


def main():
    ping()


if __name__ == "__main__":
    main()
