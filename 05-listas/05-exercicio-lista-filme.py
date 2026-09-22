# Crie um programa que permita cadastrar filmes em uma lista.

# O programa deve pedir o nome de um filme.

# Enquanto o usuário não digitar "sair", adicione o filme na lista.

# Se o filme for "Batman", mostre:
# "Você adicionou Batman!"

# Quando o usuário digitar "sair", mostre todos os filmes cadastrados.

# Exemplo:

# Digite um filme: Avatar
# Digite outro filme ou sair: Batman
# Você adicionou Batman!
# Digite outro filme ou sair: Titanic
# Digite outro filme ou sair: sair

# Filmes cadastrados:
# ['Avatar', 'Batman', 'Titanic']
filmes_cadastrados = []
filme = input("Escolha um filme: ")
print("Você adicionou", filme)

while filme != "sair":
    filmes_cadastrados.append(filme)
    filme = input("Digite outro filme: ")
    print("Você adicionou", filme)

print("Lista finalizada: ")

for filme in filmes_cadastrados:
    print("-", filme)