# Crie uma função que recebe 3 números e exiba o maior deles.

def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        maiornun = n1
    elif n2 > n1 and n2 > n3:
        maiornun = n2
    else:
        maiornun = n3
    print('O maior número é: ', maiornun)

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

maior(num1, num2, num3)