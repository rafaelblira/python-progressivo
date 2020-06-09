import random

class CaraCoroa:
    def __init__(self):
        self.lado = 'Cara'

    def lancar(self):
        if (random.randint(0,1))%2 == 0:
            self.lado = 'Cara'

        else:
            self.lado = 'Coroa'
        return self.lado

moeda = CaraCoroa()
op=1

while op:
    op=int(input('0.Sair\n'
    '1.Jogar de novo\n'))

    if op:
        print(moeda.lancar())
