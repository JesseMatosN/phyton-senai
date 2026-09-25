# Função que apresenta cauculo:
inputnumero1 = int(input("Digite um numero: "))
inputnumero2 = int(input("Digite um numero: "))
    
def somar(numero1, numero2):
    soma = numero1 + numero2
    print(soma)

# Soma
somar(inputnumero1, inputnumero2)

def subtracao(numero1, numero2):
    sub = numero1 - numero2
    print(sub)

# Subtração
subtracao(inputnumero1, inputnumero2)

def multiplicacao(numero1, numero2):
    mult = numero1 * numero2
    print(mult)

# Multiplicacão
multiplicacao(inputnumero1, inputnumero2)

def divisao(numero1, numero2):
    div = numero1 / numero2
    print(div)
    if numero2 == 0:
        print("Erro")
    
# Divisão
divisao(inputnumero1, inputnumero2)