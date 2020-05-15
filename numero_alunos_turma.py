quant = int(input('Quantas turmas? '))
cont = 0
alunos = 0
turma = [None] * quant
while cont < quant:
    
    alunos = int(input('Quanto alunos há na {}ª turma? '.format(cont + 1)))
    if alunos <= 40:
        turma[cont] = alunos
        cont += 1
    else:
        print('A turma não pode ter mas de 40 alunos')

print('O total de alunos por turma é:')
elementos = quant
cont2 = 0
n = cont2
while  cont2 < elementos:
    print('\n{}ª turma: {}'.format((cont2 + 1), (turma[n])))
    cont2 += 1
    n += 1