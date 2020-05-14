nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
salario = float(input('Qual é o seu salário: '))
sexo = str(input('Qual é o sexo [M/F]: ')).strip().upper()[0]
estadocivil = str(input('Qual é o seu extado civil:')).strip().upper()[0]
while True:
    if len(nome) < 3:
        print('nome deve ter mais de 3 caractéres')
        nome = str(input('Digite seu nome: '))
    if idade < 0 or idade > 150:
        print('idade deve ter entre 0 e 150 anos')
        idade = int(input('Digite sua idade: '))
    if salario < 0:
        print('valor de salário inválido')
        salario = float(input('Qual é o seu salário: '))
    if sexo not in 'MF':
        print('sexo inválido')
        sexo = str(input('Qual é o sexo [M/F]: ')).strip().upper()[0]
    if estadocivil not in 'SCVD':
        print('Estado civil inválido')
        estadocivil = str(input('Qual é o seu extado civil:')).strip().upper()[0]
    else:
        print('cadastro validado')
        break


