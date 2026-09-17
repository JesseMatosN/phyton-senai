# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

#
produto = (input("nome do produto: "))
preco = float(input("Preço: "))
q_c = int(input("Qunatidade comprada: "))

soma = preco * q_c

print(f"Produto: {produto}")
print(f"Preço: {preco}")
print(f"Quantidade comprada: {q_c}")
print(f"Valor final da compra: {soma}")