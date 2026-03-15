# 14. Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

# DECLARAÇÃO DE VARIÁVEIS
angle1: float = 0.0
angle2: float = 0.0
angle3: float = 0.0

# INICIO
angle1 = float(input("Digite o ângulo 1 (em graus): "))
angle2 = float(input("Digite o ângulo 2 (em graus): "))
angle3 = 180 - angle1 - angle2
print(f"O terceiro ângulo tem {angle3:,.1f}°")
# FIM
