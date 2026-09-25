# Crie uma função exibir_perfil() que receba o nome, a idade e o tipo de conta de um utilizador. 
# O tipo de conta deve ter "Gratuito" como valor padrão. 
# Teste a função com e sem informar o tipo de conta.

# Utilizador: Ana Silva | Idade: 28 | Plano: Gratuito
# Utilizador: João Santos | Idade: 35 | Plano: Premium

# Crie uma função exibir_perfil() que receba o nome, a idade e o tipo de conta de um utilizador. 
# O tipo de conta deve ter "Gratuito" como valor padrão. 
# Teste a função com e sem informar o tipo de conta.

# Utilizador: Ana Silva | Idade: 28 | Plano: Gratuito
# Utilizador: João Santos | Idade: 35 | Plano: Premium

nome = input("Seu nome: ")
idade = input("Sua idade:")


def exibirPerfil(plano = "Gratuito"):
    print(f"nome: {nome} || Idade: {idade} seu plano: {plano}")

exibirPerfil()
    
    