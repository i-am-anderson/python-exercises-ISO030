# 8. Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

# DECLARAÇÃO DE VARIÁVEIS
deposit: float = 0.0
balance: float = 0.0
rate: float = 0.013
term: int = 1

# INICIO
deposit = float(input("Digite um valor a depositar: R$ "))
balance = deposit * ((1 + rate) ** term)
print(
    f"O valor final da aplicação após {term} mês, com taxa de juros de {rate * 100}% a. m., será de R$ {balance:,.2f}")
# FIM
