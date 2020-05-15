quant = int(input('Quantas provas? '))
cont = 0
soma = 0
media = 0
while cont < quant:
    nota = float(input('Qual foi a nota da {}º prova? '.format(cont + 1) ))
    cont += 1
    soma += nota
    media = soma / quant
print('A média do aluno foi: ', media)


