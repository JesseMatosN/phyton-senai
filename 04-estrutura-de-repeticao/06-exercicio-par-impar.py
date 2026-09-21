# Cria um programa que percorra os números de 1 a 10 
# e mostre se cada número é par ou ímpar.

numeros = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10}

for numero in numeros:
    if numero % 2 == 0:
        print(f"numero par: {numero}")
print("=============")
for numero in numeros:
    if numero % 2 != 0:
        print(f"numero impar: {numero}")
