# Cria um programa que peça um número ao utilizador e mostre a 
# tabuada desse número de 1 a 10, utilizando um ciclo for.

# Digite um número: 5

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50


n = int(input("Digite um numero para ser multiplicado até 10: "))

for i in range(1, 11):
    resultado = n * i
    print(n, "x", i, "=", resultado)