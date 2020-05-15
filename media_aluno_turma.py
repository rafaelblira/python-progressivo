#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos
quant = int(input('Quantas turmas: '))
cont = 0
alunos = 0
soma = 0
media = 0
while cont < quant:
    alunos = int(input('Quantos alunos há na {}ª turma? '.format(cont + 1)))
    if alunos < 40:
        cont += 1
        soma += alunos
    else:
        print('A quantidade de alunos por turma não pode exceder a 40.')
media = soma / quant
print('A média de alunos por turma é:', media)