# 16. Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

# DECLARAÇÃO DE VARIÁVEIS
hours_worked: float = 0.0
hourly_rate: float = 0.0
discount_percent: float = 0.0
num_dependents: int = 0
gross_salary: float = 0.0
net_salary: float = 0.0

# INICIO
hours_worked = float(input("Digite quantas horas foram trabalhadas: "))
hourly_rate = float(input("Digite o valor por hora (R$): "))
discount_percent = float(input("Digite o percentual de desconto (%): "))
num_dependents = int(input("Digite a quantidade de dependentes: "))
gross_salary = hours_worked * hourly_rate
net_salary = gross_salary * (1 - discount_percent / 100) + 100 * num_dependents
print(
    f"O salário a ser recebido (líquido) é de R$ {net_salary:,.2f}")
# FIM
