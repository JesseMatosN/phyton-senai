# Tupla contendo outras tuplas
alunos = (
    ("Carlos", 17,),
    ("Ana", 18),
    ("João", 16)
)

# Acessando a primeira tupla
print(alunos[0])

print(alunos[0][0])

print(alunos[0][1])

for aluno in alunos:
    print(f"Nome: {aluno[0]}")
    print(f"Idade: {aluno[1]}")
    print("-----------")