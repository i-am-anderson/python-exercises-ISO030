def main():
    vector1: int = [0] * 100
    bigger: int = 0
    smaller: int = 0
    sum: int = 0
    avg: float = 0.0

    for i in range(len(vector1)):
        vector1[i] = int(input(f"Digite o valor do elemento {i}: "))
        sum += vector1[i]
        if vector1[i] > bigger:
            bigger = vector1[i]
        if vector1[i] < smaller:
            smaller = vector1[i]

    avg = sum / len(vector1)
    print(f"O maior valor é: {bigger}")
    print(f"O menor valor é: {smaller}")
    print(f"A média dos valores é: {avg}")


if __name__ == "__main__":
    main()
