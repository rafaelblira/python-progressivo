quant = int(input('Quantas pessoas há no grupo? '))
cont = 0
jovem = 0
adulto = 0
idoso = 0
soma = 0
media = 0
while cont < quant:
    idade = int(input('Qual é a idade da {}ª pessoa? '.format(cont + 1)))
    soma += idade
    media = soma / quant
    cont += 1
    if  0 <= idade <= 25:
        jovem += 1
    if 26 <= idade <= 60:
        adulto += 1
    if idade > 60:
        idoso += 1
print('Jovens: {}, adultos: {} e idosos: {}'.format(jovem, adulto, idoso))
print('A média de idade do grupo: ', media)
