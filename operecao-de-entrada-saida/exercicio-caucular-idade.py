"""
Faça um programa que peça o ano de nascimento de uma pessoa
e calcule a sua idade atual.
Depois, mostre o ano de nascimento e a idade no terminal.
"""

# Entrada de dados
pessoa = (input("Nome: "))
data_n = int(input("Data de nascimento: "))


# Processamento computacional
idade_ano = 2026 - data_n

# Saída de informações
print(f"Ano de nascimento: {data_n}")
print(f"idade: {idade_ano}")
