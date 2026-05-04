def main():
    vector1: int = [0] * 50
    sum1: float = 0.0
    sum2: int = 0
    avg: float = 0.0
    count: int = 0

    for i in range(len(vector1)):
        vector1[i] = int(input(f"Digite o valor do elemento {i}: "))

        if vector1[i] >= 10 and vector1[i] <= 200:
            sum1 += vector1[i]
            count += 1
        if vector1[i] % 2 != 0:
            sum2 += vector1[i]

    avg = sum1 / count if sum1 > 0 else 0

    print(f"A média dos valores entre 10 e 200 é: {avg}")
    print(f"A soma dos valores ímpares é: {sum2}")


if __name__ == "__main__":
    main()
