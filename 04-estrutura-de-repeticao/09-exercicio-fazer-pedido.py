# Cria um programa que permita ao utilizador fazer vários pedidos numa lanchonete.

# O programa deve pedir ao utilizador o nome de um produto.

# Enquanto o utilizador não escrever sair, o programa deve continuar a pedir novos produtos.

# Quando o utilizador escrever sair, o programa deve mostrar:

#   .Quantos produtos foram pedidos;
#   .Uma mensagem a indicar que o pedido foi finalizado.

# Digite o produto que deseja pedir: hambúrguer
# Digite o produto que deseja pedir: batata
# Digite o produto que deseja pedir: refrigerante
# Digite o produto que deseja pedir: sair

# Pedido finalizado!
# Você pediu 3 produtos.
compras = []
quant = 0

pedido = input("seu pedido: ")

while pedido != "sair":
    compras.append(pedido)
    quant = quant + 1

    pedido = input("Digite outro produto: ")

print("pedido finalizado!")
print(quant)

for produto in compras:
    print("-", pedido)

  

