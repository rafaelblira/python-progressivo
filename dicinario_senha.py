loginSenha={'joao'   : 'rush',
             'maria'  : 'yes', 
            'zezinho': 'genesis'}

login = str(input('Login: '))
senha = str(input('Senha: '))

if loginSenha[login] == senha:
    print('Acesso autorizado')
else: 
    print('Senha errada')