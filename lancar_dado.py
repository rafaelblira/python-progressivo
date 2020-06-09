import random

class Dado():
    def __init__(self):
        self.lado = 1

    def lancar(self):
        return random.randint(1,6)

dado = Dado()
op = 1

while op:
    op = int(input('0. Sair\n1.Lançar Dado\n'))
    if op:
        print('O lado do dado é: ', dado.lancar())
1