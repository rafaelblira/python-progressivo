def somatres(n1, n2, n3):
    return n1 + n2 + n3
    
def mediatres(nun):
    return nun/3

def menu():
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    n3 = int(input('Terceiro número: '))

    print('Soma: ', somatres(n1, n2, n3))
    print('Média: ', mediatres(somatres(n1,n2, n3)))
    print('=-'*30)

while True:
    menu()



