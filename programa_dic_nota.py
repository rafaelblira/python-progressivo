def menu():
    opcao = 1

    while opcao:
        opcao = int(input('Digite uma das seguintes opções: \n0. Sair \n1. Exibir lista de alunos com suas notas \n2. Inserir aluno e nota\n3. Alterar a nota de um aluno\n4. Consultar nota de um aluno específico\n5. Apagar um aluno da lista\n6. Dar a média da turma\n'))



        if opcao == 1:
            exibir()            

        elif opcao == 2:
            inserir()            

        elif opcao == 3:
            alterar()
            
        elif opcao == 4:
            consultar()
            
        elif opcao == 5:
            apagar()
                
        elif opcao == 6:
            media()

        elif opcao == 0:
            print('Encerrando o programa')
            
        else:
            print("Opção inválida")

def exibir():
    for nome in notas.keys(): #funcao keys checa se a chave está no dicionario
        print(nome,' tirou nota: ', notas[nome])

def inserir():
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Nota dele: "))
    if notas.get(nome): #funcao get checa que já existe a chave na lista para impedir duas chaves iguais
        print("Ja existe o aluno ",nome)
    else:
        notas[nome] = nota
        print(notas)

def alterar():
    nome = input("Aluno a mudar a nota: ")
    nota = float(input("Nova nota     : "))

    if nome in notas.keys():
        notas[nome] = nota
    else:
        print("Não existe esse aluno")
    print(notas)

def consultar():
    nome = input("Digite o nome do aluno que deseja consultar nota: ")

    if nome in notas.keys():
        print(notas[nome]) #imprime somente a nota do aluno
    else:
        print("Não existe esse aluno")

def apagar():
    nome = input("Digite o nome do aluno que apagar: ")

    if nome in notas.keys():
        notas.pop(nome) #apago somente o aluno informado
        print(notas)
    else:
        print("Não existe esse aluno")

def media():
    cont = 0
    soma = 0
    for c in notas.values(): #seleciona somente os valores das notas
        cont += 1
        soma += c
    media = soma / cont
    print('A media da turma é: ', media)


notas={}
menu()
