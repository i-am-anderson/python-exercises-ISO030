# 4. Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.

# DECLARAÇÃO DE VARIÁVEIS
temperature_celsius: float = 0.0
temperature_fahrenheit: float = 0.0

# INICIO
temperature_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperature_fahrenheit = (9 * temperature_celsius + 160) / 5
print(f"A temperatura em Fahrenheit é {temperature_fahrenheit:,.1f}",)
# FIM
