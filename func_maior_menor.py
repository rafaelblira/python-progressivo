#Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número através de outra função.

def maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def menor(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
print('O maior número é: ', maior(n1, n2, n3))
print('O menor número é: ', menor(n1, n2, n3))