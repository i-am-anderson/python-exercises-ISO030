# 1. Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.

# DECLARAÇÃO DE VARIÁVEIS
side: float = 0.0
area: float = 0.0

# INICIO
side = float(input("Digite o lado do quadrado: "))
area = side ** 2
print(f"A área do quadrado é de ~ {area:,.2f}")
# FIM
