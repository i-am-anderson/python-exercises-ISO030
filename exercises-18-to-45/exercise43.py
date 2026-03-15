# 43. Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

# DECLARAÇÃO DE VARIÁVEIS
ana_height: float = 1.1
ana_ratio: int = 3
maria_height: float = 1.5
maria_ratio: int = 2
years: int = 0

# INICIO
while (ana_height <= maria_height):
    ana_height += ana_ratio / 100
    maria_height += maria_ratio / 100
    years += 1
print(f"Serão necessários {years} anos para que Ana seja maior que Maria")
# FIM
