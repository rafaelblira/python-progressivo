# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
# consertar código
codigo = 1
peso = 0
altura = 0
magro = 0
gordo = 0
alto = 0
baixo = 0
cod_gordo = 0
cod_magro = 0
cod_alto = 0
cod_baixo = 0
soma_altura = 0
soma_peso = 0
media_altura = 0
media_peso = 0
cont = 0
while codigo != 0:
    codigo = int(input('Código do cliente: '))
    if codigo != 0:
        magro = peso
        gordo = peso
        alto = altura
        baixo = altura     
        cont += 1
        peso = float(input('Peso: ')) 
        altura = float(input('Altura: '))

        if peso > gordo:
            gordo = peso
            cod_gordo = codigo
        if altura > alto:
            alto = altura
            cod_alto = codigo
        if peso < magro:
            magro = peso
            cod_magro = codigo
        if altura < baixo:
            baixo = altura
            cod_baixo = codigo
        soma_altura += altura
        soma_peso += peso
media_altura = soma_altura / cont
media_peso = soma_peso / cont   
print('Mais alto: {}, código:{}'.format(alto, cod_alto))
print('Mais baixo: {}, código: {} '.format(baixo, cod_baixo))
print('Mais magro: {}, código: {}'.format(magro, cod_magro))
print('Mais gordo: {}, código: {}'.format(gordo, cod_gordo))
print('Media da altura: {:.2f}'.format(media_altura))
print('Média de peso: {:.2f}'.format(media_peso))
    