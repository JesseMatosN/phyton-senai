compras = []
produto = input("Digite um produto (ou 'fim' para terminar): ")

while produto != "fim":
    compras.append(produto)

    produto = input("digite outro produto (ou 'fim' para terminar): ")

    print(compras)

print("Lista de compras: ")

for produto in compras:

    print("-", produto)

