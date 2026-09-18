# Faça um programa em Python que peça a nota de um aluno 
# e verifique se ele foi aprovado ou reprovado.

# Nota maior ou igual a 6 → Aprovado
# Nota menor que 6 → Reprovado

nota = float(input("Nota: "))

if nota >= 6:
    print("Passou de anoo, parabens!")
else:
    print("Reprovado, se dedique mais!")