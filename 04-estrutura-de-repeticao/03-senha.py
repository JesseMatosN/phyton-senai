# Define a senha correta
senha_correta = "1234"

# Solicita a senha do usuario
senha = input("Digite sua senha: ")

# Enquanto a senha estiver errado 
while senha != senha_correta:

    # Informa que a senha esta errada  
    print("Senha incorreta!")

    # solicita a senha novamente
    senha = input("Digite a senha novamente: ")

# Quando a condição ficar falsa, a senha esta correta
print("Senha correta! Acesso permitido")
