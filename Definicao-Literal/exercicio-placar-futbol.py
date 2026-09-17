
# Praticar variáveis, números inteiros, operações matemáticas e f-strings.

# Descrição:
# Crie um programa que represente o resultado de uma partida de futebol.
#  O programa deve armazenar o nome de dois times 
#  e a quantidade de gols marcados por cada equipa.

# Depois, apresente o placar e calcule o total de gols da partida.

# Resultado no terminal
# ================================
#         RESULTADO DO JOGO
# ================================
# França 3 x 2 Espanha
# Total de gols: 5
# ================================

time1 = "França"
time2 = "Espanha"
placar1 = 3
placar2 = 2
placar_total_de_gols = placar1 + placar2

print("=====================================================")
print("                RESULTADO DO JOGO                    ")
print("=====================================================")   

print(f"{time1} fez {placar1} gols e a {time2} fez {placar2}\n")

print("total de gols desse jogo: ", placar_total_de_gols)