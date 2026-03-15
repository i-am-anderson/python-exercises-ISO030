# 10. Receba 2 números reais. Calcule e mostre a diferença desses valores.

# DECLARAÇÃO DE VARIÁVEIS
a: float = 0.0
b: float = 0.0
c: float = 0.0

# INICIO
a = float(input("Digite o primeiro número real: "))
b = float(input("Digite o segundo número real: "))
c = a - b
print(f"A diferença entre {a:,.2f} e {b:,.2f} é {c:,.2f}")
# FIM
