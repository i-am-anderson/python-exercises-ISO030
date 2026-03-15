# 27. Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

# DECLARAÇÃO DE VARIÁVEIS
n_voltas: int = 0
e_circuito: int = 0
t_duracao: int = 0
v_media: int = 0
ext: int = 0

# INICIO
while (n_voltas <= 0 and e_circuito <= 0 and t_duracao <= 0):
    n_voltas = int(input("Digite o número de voltas: "))
    e_circuito = int(input("Digite a extensão do circuito (metros): "))
    t_duracao = int(input("Digite o tempo de duração (minutos): "))

ext = n_voltas * e_circuito
v_media = (ext / 1000) / (t_duracao / 60)
print(f"A velocidade média é de {v_media}km/h")
# FIM
