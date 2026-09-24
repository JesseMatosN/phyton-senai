# Crie uma lista com algumas comidas e seus respectivos tipos.

# Percorra a lista usando um for.

# Se o tipo da comida for "Doce", mostre o nome da comida.

# Resultado:

# Comida doce: Brigadeiro
# Comida doce: Pudim

comidas = [
    ["Pizza", "Salgado"],
    ["Brigadeiro", "Doce"],
    ["Hambúrguer", "Salgado"],
    ["Pudim", "Doce"]
]

for comida in comidas:
    if comida[1] == "Doce":  # Alterado para "Doce"
         print(f"comida doce:    {comida[0]}")
    else:
        print(f"comida salgada: {comida[0]}")
