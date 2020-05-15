#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
quant = int(input('Digite a quantidade de CDs: '))
cont = 0
soma = 0
media = 0
produto = 0
while cont < quant:
    produto = float(input('Quanto custou o {}º CD? R$ '.format(cont + 1)))
    cont += 1
    soma += produto
media = soma / quant
print('O valor total investido é R$ {:.2f} e o valor médio gasto foi R$ {:.2f}'.format(soma, media))
