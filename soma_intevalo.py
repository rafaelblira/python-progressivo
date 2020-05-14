numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = 0
for n in range(numero1 + 1, numero2):
    soma += n
print(soma)