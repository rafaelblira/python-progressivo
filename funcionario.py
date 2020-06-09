class Funcionario:
    count = 0
    def __init__(self, nome):
        self.__nome = nome
        print(nome, 'contratado!')
        Funcionario.count += 1
        print('Numero de funcionarios: ', Funcionario.count)

op = 1
func = []

while op:
    op = int(input('0. Sair\n1. Criar funcionario\n '))

    if op == 1:
        nome = input('Nome: ')
        func.append(Funcionario(nome))