quantidade = int(input('Digite a quantidade de números: '))
numero = int(input('Digite um numero: '))
maior = numero
soma = numero

for cont in range (quantidade - 1):
    numero = int(input('Digite outro numero: '))   
    if numero > maior:
        maior = numero
    soma += numero
    media = soma / quantidade
       
print('O maior número foi: ', maior)
print('A soma foi: ', soma)
print('A média foi: ', media)

