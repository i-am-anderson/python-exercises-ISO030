# 38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

# DECLARAÇÃO DE VARIÁVEIS
count: int = 0
num: int = 0
bigger: int = 0
smaller: int = 0

# INICIO
while (count < 100):
    num = int(input(f"Digite o {count + 1}° número: "))
    if (num > 0):
        if (count == 0):
            bigger = smaller = num
        else:
            if (num > bigger):
                bigger = num
            elif (num < smaller):
                smaller = num
        count += 1

print(
    f"O maior valor digitado foi: {smaller} - O menor valor digitado foi: {bigger}")
# FIM
