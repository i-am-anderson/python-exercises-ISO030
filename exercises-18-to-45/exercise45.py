# 45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 - ... + 15/225

# DECLARAÇÃO DE VARIÁVEIS
sum_: float = 0

# INICIO
print("SÉRIE:")
for x in range(1, 16):
    if (x != 1):
        print(f"{x}/{x ** 2}", end="")
    else:
        print("1", end="")

    if (x % 2 == 0 and (x < 16 - 1)):
        sum_ -= (x/x ** 2)
        print(" + ", end="")
    elif (x % 2 != 0 and (x < 16 - 1)):
        sum_ += (x/x ** 2)
        print(" - ", end="")
    else:
        sum_ += (x/x ** 2)
        print(" = ", end="")
print(f"{sum_:,.2f}", end="")
# FIM
