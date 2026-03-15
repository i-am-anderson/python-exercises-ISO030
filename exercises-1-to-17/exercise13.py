# 13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

# DECLARAÇÃO DE VARIÁVEIS
quantity_kg: float = 0.0
duration_days: int = 0
consumption_g_per_day: float = 50

# INICIO
quantity_kg = float(input("Insira a quantidade de alimento (em quilos): "))
duration_days = round((quantity_kg * 1000) / consumption_g_per_day)
print(f"{quantity_kg:,.2f} kg de alimentos durará cerca de {duration_days} dias, considerando que o consumo será de {consumption_g_per_day} g/dia")
# FIM
