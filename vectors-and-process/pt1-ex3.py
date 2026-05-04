def main():
    vector1: float = [0.0] * 30
    sum: float = 0.0
    avg: float = 0.0
    above_avg_count: int = 0
    index_bellow_avg: int = []

    for i in range(len(vector1)):
        vector1[i] = float(input(f"Digite o valor do elemento {i}: "))
        sum += vector1[i]

    avg = sum / len(vector1)

    for i in range(len(vector1)):
        if vector1[i] > avg:
            above_avg_count += 1
        else:
            index_bellow_avg.append(i)

    print(f"A média do grupo é: {avg}")
    print(f"A quantidade de notas acima da média: {above_avg_count}")
    print(f"Os índices das notas abaixo da média: {index_bellow_avg}")


if __name__ == "__main__":
    main()
