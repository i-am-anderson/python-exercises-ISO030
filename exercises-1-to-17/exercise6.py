# 6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

# DECLARAÇÃO DE VARIÁVEIS
x: str = ""
y: str = ""

# INICIO
x = input("Digite um valor para x: ")
y = input("Digite um valor para y: ")
x, y = y, x
print(f"O novo valor de X é {x} e o novo valor de Y é {y}")
# FIM
