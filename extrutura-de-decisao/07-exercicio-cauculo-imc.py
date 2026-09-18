# Faça um programa em Python que peça o peso (kg) 
# e a altura (m) de um indivíduo. Calcule o IMC
# mostre a sua classificação:

# Menor que 18,5: abaixo do peso
# De 18,5 a 24,9: peso normal
# 25 ou mais: acima do peso

peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

cauculo = peso / (altura * altura)
print(f"seu imc: {cauculo}")

if cauculo <= 18.5:
    print("Abaixo do peso")
elif cauculo >= 18.5 and cauculo < 24.9:
    print("Peso normal")
else:
    print("Acima do peso")