# 12. Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

# DECLARAÇÃO DE VARIÁVEIS
birth_year: int = 0
current_year: int = 0
age: int = 0
future_age: int = 0
future: int = 17

# INICIO
birth_year = int(input("Digite o ano em que você nasceu: "))
current_year = int(input("Digite o ano atual: "))
age = current_year - birth_year
future_age = age + future
print(
    f"Atualmente você tem {age} anos. Daqui a {future} anos você terá {future_age}!")
# FIM
