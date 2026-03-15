# 39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N

# DECLARAÇÃO DE VARIÁVEIS
casa: int = 1
qtde: int = 1

# INICIO
for i in range(0, 64, 1):
    print(f"Casa: {i + 1} - Qtde: {2**i}")
# FIM
