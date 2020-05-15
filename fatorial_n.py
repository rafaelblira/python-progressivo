#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

fatorial = int(input('Digite um número para saber o fatorial: '))
nfat = fatorial
for cont in range(1, fatorial):
    fatorial *= cont
print('Farorial de: {}'.format(nfat))
print('{}! ='.format(nfat), end=' ')
for i in range(nfat, 2, -1):
    print(i, end=' . ')
print('1 =',fatorial)