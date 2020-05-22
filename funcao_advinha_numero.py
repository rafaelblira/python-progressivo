from random import randint
a = randint(1, 100)
def advinha(n):
    if n == a:
        return'Acertou!'
               
    elif n > a:
        return'Menos'
            
    else:
        return'Mais'       
    
    
tentativa = 0
while True:
    tentativa += 1
    numero = int(input('Digite um número de 1 a 100: '))
    print(advinha(numero))
    if numero == a:
        print('Tentativas: {}'.format(tentativa))
        break
    