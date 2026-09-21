# Entradas de dados basicos
nome = input("Informe seu nome: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

# Processamento computacional
media = (n1 + n2) / 2

# Saída das informações
print(f"A media do aluno: {nome}")
# Formatação com uma casa decimal
# f ==> significa numero de ponto flutuante (decimal)
# .1 ==> siginifica mostrar 1 casa decimal
print(f"Media final: {media: .1f}")