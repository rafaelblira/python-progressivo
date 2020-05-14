par = 0
impar = 0
for c in range (1, 11):
    numero = int(input('Digite o {}º número: '.format(c)))
    if numero % 2 ==0:
        par += 1
    else:
        impar += 1
print('Quantidade de números pares: ', par, '\nQuantidade de números ímpares: ', impar)