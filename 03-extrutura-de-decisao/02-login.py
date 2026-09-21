# Solicita o login do usuario
login = input("digite seu login: ")

# Solicita a senha do usuario
senha = int(input("Digite sua senha: "))

# Verifica se o login e a senha estão corretos
if login == "admin" and senha == "1234":
    print("Seja bem-vindo, Admin!")
else:
    print("Login ou senha incorretos!")



