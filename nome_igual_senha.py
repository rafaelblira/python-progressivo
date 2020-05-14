nome = str(input('Digite o nome de usuário: '))
senha = str(input('Digite uma senha: '))
while True:
    if nome == senha:
        print('Sua senha deve ser diferente do login:')
        nome = str(input('Digite o nome de usuário: '))
        senha = str(input('Digite uma senha: '))
    else:
        print('senha válida')
        break

