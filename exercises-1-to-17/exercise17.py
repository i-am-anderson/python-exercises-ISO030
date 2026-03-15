# 17. Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

# DECLARAÇÃO DE VARIÁVEIS
quantity_l: float = 0.0
consumption_km_per_l: int = 12
time: float = 0.0
avg_speed: float = 0.0

# INICIO
time = float(input("Digite o tempo do percurso (horas): "))
avg_speed = float(input("Digite a velocidade média do percurso (km/h): "))
quantity_l = (avg_speed * time) / consumption_km_per_l
print(f"Um veículo que consome {consumption_km_per_l} km/l fazendo um percurso de {time:,.2f} hora(s) a uma velocidade média de {avg_speed:,.2f} km/h, consumirá {quantity_l:,.2f} litros de combustível!")
# FIM
