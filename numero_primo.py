numero = int(input('Digite um número para saber se ele é primo: '))
mult = 0
for cont in range(2, numero):
    if numero % cont == 0:
        mult += 1
        print(cont, end=' ')
print('\ntem {} multiplos'.format(mult))
if mult == 0:
    print('é primo')

    