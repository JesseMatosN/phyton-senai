# 18 anos ou mais: Pode entrar na festa.
# 16 ou 17 anos: Pode entrar com responsável.
# Menos de 16 anos: Não pode entrar na festa.

idade = int(input("Sua idade: "))

if idade >= 18:
    print("Pode entrar na festa")
elif idade >= 16 and idade < 18:
    print("Pode entrar na festa com responsavel")
else:
    print("Não pode entra na festa")
