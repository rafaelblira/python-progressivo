#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário
numero = int(input('Montar tabuada de: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar em: '))
for c in range(inicio, fim + 1):
    if fim > inicio:
        print(numero, ' x ', c, ' = ', numero * c)
   