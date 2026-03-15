# 41. Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.

# DECLARAÇÃO DE VARIÁVEIS

# INICIO
for n1 in range(7):
    for n2 in range(7):
        if (n1 + n2 == 7):
            print(f"({n1},{n2})")
# FIM
