frutas = ["Maça", "Banana", "Laranja"]

#Index()
print(f"Index(): {frutas.index("Banana")}") # Mosta a posição

# Count
print(f"Count(): {frutas.count("Banana")}") # Conta a contidade desse item

# Apeend
frutas.append("Uva") # adicionado 
print(f"append(): {frutas}") # adicionando "Uva" a lista

# Extend()
outras_frutas = ["abacaxi", "Morango"]
frutas.extend(outras_frutas)
print(f"Extend(): {frutas}")