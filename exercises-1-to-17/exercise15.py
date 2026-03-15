# 15. Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

# DECLARAÇÃO DE VARIÁVEIS
side1: float = 0.0
side2: float = 0.0
side3: float = 0.0

# INICIO
side1 = float(input("Insira o primeiro cateto: "))
side2 = float(input("Insira o segundo cateto: "))
side3 = (side1 ** 2 + side2 ** 2) ** 0.5
print(
    f"A hipotenusa é a raiz quadrada da soma dos quadrados de {side1:,.2f} e {side2:,.2f}, portanto hipotenusa = {side3:,.2f}")
# FIM
