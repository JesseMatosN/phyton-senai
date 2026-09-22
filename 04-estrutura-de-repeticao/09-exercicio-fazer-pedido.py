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
lista = []
pedido = input("Escolha um lanche (ou digite 'sair'): ")
quant = 0

while pedido != "sair":
    lista.append(pedido)
    quant = quant + 1
    pedido = input("Escolha outro lanche (ou digite 'sair'): ")

print("Pedido finalizado")
print(f"total: {quant} lanches")

for pedido in set(lista):
    repitido = lista.count(pedido)
    print(repitido, "x -", pedido)