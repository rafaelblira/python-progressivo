# Crie uma função que recebe 4 notas de um aluno, e exiba a média dele.
def media(n1, n2, n3, n4):
    resultado = (n1 + n2 + n3 + n4)/ 4
    print('A média do aluno é {}'.format(resultado))

nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
nota3 = int(input('Terceira nota: '))
nota4 = int(input('Quarta nota: '))
media(nota1, nota2, nota3, nota4)