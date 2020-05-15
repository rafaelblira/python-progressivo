#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperatura = 0
cont = 0
soma = somat = 0
media = 0
maior = 0
menor = 999
opcao = ''
while opcao in 'S':
    temperatura = float(input('Qual a temperatura? '))
    cont += 1
    soma += temperatura
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    media = soma / (cont)  
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    
print('Menor temperatura: {}ºC'.format(menor))
print('Maior temperatura: {}ºC'.format(maior))
print('Temperatura média: {}ºC'.format(media))

