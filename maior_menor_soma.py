while True:
    quant = int(input('Quantos números quer digitar? '))
    if quant < 0 or quant > 1000:
        print('O número tem que ser entre 0 e 1000')
    else:
        numero = int(input('Digite o 1º número: '))
        maior = numero
        soma = numero
        for c in range(quant - 1):
            numero = int(input('Digite o {}º um número: '.format(c + 2)))
            if numero > maior:
                maior = numero
            soma += numero
        print('maior: ', maior)
        print('soma: ', soma)




