nota = int(input('Digite uma nota entre 0 e 10: '))
while True:
    if nota < 0 or nota > 10:
        print('Valor inválido, tente novamente')
        nota = int(input('Digite uma nota entre 0 e 10: '))
    else:
        print('nota válida')
        break
    
            

    

    
