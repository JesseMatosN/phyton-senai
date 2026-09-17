"""
Faça um programa que peça o nome de um time de futebol,
a quantidade de vitórias e empates.
Sabendo que cada vitória vale 3 pontos e cada empate vale 1 ponto,
calcule e mostre a pontuação total do time.

"""
# Entrada de dados
t1 = (input("nome do seu time: "))
pontuacao_do_t1 = int(input("Pontuação: "))
empates = int(input("Empates: "))

# Processamento computacional

cauculo_pontos = (pontuacao_do_t1 * 3) + empates

# Saída de informações 
print(f"seu time {t1}")
print(f"pontuação total do seu time: {cauculo_pontos}")

