while True:
    texto = str(input('Digite uma frase:'))
    if texto.isupper():
        print('Tudo maiusculo')
    elif texto.islower():
        print('Tudo minúsculo')
    else:
        print('Misturado')
