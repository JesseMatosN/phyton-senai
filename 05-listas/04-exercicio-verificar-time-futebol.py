# Crie um programa em Python que tenha uma lista com alguns times de futebol.

# Peça para o usuário digitar o nome de um time.

# Verifique se o time digitado está na lista.

# Se estiver, mostre:
# "Esse time está na lista!"

# Caso contrário, mostre:
# "Esse time não está na lista!"

# times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]
times = ["São paulo", "corinthias", "Palmeiras"]

time = input("time: ")

if time in times:
    print("Esta na lista!")
else:
    print("Não esta na lista!")