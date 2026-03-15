# 21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#   a. Se a média for >= 6,0 exibir “APROVADO”;
#   b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
#   c. Se a média for < 3,0 exibir “RETIDO”.

# DECLARAÇÃO DE VARIÁVEIS
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
avg: float = 0.0

# INICIO
n1 = float(input("Insira a nota N1: "))
n2 = float(input("Insira a nota N2: "))
n3 = float(input("Insira a nota N3: "))
n4 = float(input("Insira a nota N4: "))
avg = (n1 + n2 + n3 + n4) / 4
if (avg < 3):
    print(f"A média é {avg:,.2f}! Portanto aluno está 'RETIDO'")
elif (avg >= 3 and avg < 6):
    print(f"A média é {avg:,.2f}! Portanto aluno está de 'EXAME'")
else:
    print(f"A média é {avg:,.2f}! Portanto aluno está 'APROVADO'")
# FIM
