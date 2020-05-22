def positivo(p):
    if p > 0:
        print('P')
    else:
        print('N')

while True:
    numero = int(input('Digite um número: '))
    positivo(numero)