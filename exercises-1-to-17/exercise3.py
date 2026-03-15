# 3. Receba a base e a altura de um triângulo. Calcule e mostre a sua área.

# DECLARAÇÃO DE VARIÁVEIS
base: float = 0.0
height: float = 0.0
area: float = 0.0

# INICIO
base = float(input("Digite o valor da base do triângulo: "))
height = float(input("Digite o valor da altura do triângulo: "))
area = (base * height) / 2
print(f"A área do triângulo é de ~ {area:,.2f}")
# FIM
