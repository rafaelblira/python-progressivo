print('Sequência Fibonacci')
n = int(input('Digite quantos termos: '))
ultimo = 1
penultimo = 1
if n ==1 or n == 2:
    print('1')
else:
    print('1 1', end=' ')
    for cont in range (2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        cont += 1
        print (termo, end=' ')