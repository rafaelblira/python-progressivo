#Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
def celsius(f):
    cel = (5 * (f - 32)) / 9
    return cel

def fahrenheint(c):
    fah = (c * (9/5)) + 32
    return fah

def menu():
    opcao = int(input('Digite a escala termométrica para qual deseja conversão:\n1. Celcius\n2. Fahrenheint\nQual a opção? '))
    if opcao == 1:
        temperatura = int(input('Digite a temperatura em Fahrenheint: '))  
        print('{}ºF equivale a'.format(temperatura), celsius(temperatura), 'ºC')
    elif opcao == 2:
        temperatura = int(input('Digite a temperatura em Celsius: '))  
        print('{}ºC equivale a'.format(temperatura), fahrenheint(temperatura),'ºF')


while True:
    menu()
    



