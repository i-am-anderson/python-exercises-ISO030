# 28. Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
#   Venda Mensal        Preço atual           Preço Novo
#   < 500               < 30.00               + 10%
#   >= 500 e < 1000     >= 30.00 e < 80.00    + 15%
#   >= 1000             >= 80.00              - 5%
# Obs.: para outras condições, preço novo será igual ao preço atual.

# DECLARAÇÃO DE VARIÁVEIS
preco_atual: float = 0
media_mensal: int = 0
preco_novo: float = 0

# INICIO
while (preco_atual <= 0 and media_mensal <= 0):
    preco_atual = float(input("Digite o preço atual: "))
    media_mensal = int(input("Digite a media mensal: "))
if (media_mensal < 500 or preco_atual < 30.00):
    preco_novo = preco_atual * 1.1
elif ((media_mensal >= 500 and media_mensal < 1000) or (preco_atual >= 30.00 and preco_atual < 80.00)):
    preco_novo = preco_atual * 1.15
elif ((media_mensal >= 1000) or (preco_atual >= 80.00)):
    preco_novo = preco_atual * 0.95
else:
    preco_novo = preco_atual

print(f"O novo preço será: R$ {preco_novo:,.2f}")
# FIM
