#crie uma função que recebe um número e exiba seu quadrado.
def quadrado(n):
    quad = n ** 2
    print('Quadrado de {} é: {}'.format(n, quad))

numero = int(input('Digite um númeor para saber o seu quadrado: '))
quadrado(numero)