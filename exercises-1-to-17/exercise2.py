# 2. Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.

# DECLARAÇÃO DE VARIÁVEIS
salary: float = 0.0
new_salary: float = 0.0

# INICIO
salary = float(input("Digite o salário inicial: R$ "))
new_salary = salary * 1.15
print(f"O novo salário será de: R$ {new_salary:,.2f}")
# FIM
