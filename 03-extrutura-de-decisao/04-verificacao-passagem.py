# Programa: Verificação de passagem

# Faça um programa em Python que peça a idade de uma pessoa
# e verifique se ela paga passagem inteira ou meia passagem.

# Idade menor ou igual a 12 → Meia passagem
# Idade maior que 12 → Passagem inteira
idade = int(input("Sua idade: "))

if idade <= 12:
    print("Meia passagem")
else:
    print("Passagem inteira")