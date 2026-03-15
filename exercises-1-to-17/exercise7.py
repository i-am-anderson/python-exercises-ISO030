# 7. Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.

# DECLARAÇÃO DE VARIÁVEIS
length: float = 0.0
width: float = 0.0
height: float = 0.0
volume: float = 0.0

# INICIO
length = float(input("Digite um valor para o comprimento: "))
width = float(input("Digite um valor para a largura: "))
height = float(input("Digite um valor para a altura: "))
volume = length * width * height
print(f"O volume do paralelepípedo é ~ {volume}")
# FIM
