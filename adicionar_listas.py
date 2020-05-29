bandas = []

while True:
    op =int(input("1. Adicionar banda\n"
                  "2. Exibir bandas favoritas\n"
                  "3. Tamanho da lista\n"
                  "4. Mudar valor de item\n"))

    if(op==1):
        banda=input("Digite nome da banda: ")
        bandas.append(banda)
    if(op==2):
        print(bandas)
    if(op==3):
        print("Tamanho da lista: ", len(bandas))
    if(op==4):
        index=int(input("Indice que vai alterar: "))
        if(index<len(bandas)):
            temp=input("Nome da banda: ")
            bandas[index] = temp
        else:
            print("Esse indice nao existe")