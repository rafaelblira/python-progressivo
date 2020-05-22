def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    soma = x + y
    print("Soma: ",soma)

def multiplicar():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    soma = x * y
    print("Multiplicação: ",soma)

def subtrair():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    soma = x - y
    print("Subtração: ",soma)

def dividir():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    soma = x / y
    print("Divisão: ",soma)

opcao = 1
print('Qual operação você deseja fazer?\nPara somar digite [1]\nPara subtrair digite [2]\nPara multiplicar digite [3]\nPara dividir digite [4]\nPara sair digite [0]')

while opcao:
    opcao = int(input('Digite a opção: '))
    if opcao > 0 and opcao <=4:
        if opcao == 1:
            soma()
        elif opcao == 2:
            subtrair()
        elif opcao == 3:
            multiplicar()
        elif opcao == 4:
            dividir()
    