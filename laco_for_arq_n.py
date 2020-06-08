arquivo = open('linguagens.txt', 'r')
num = int(input("Numero de linguagens: "))
count=0

for linha in arquivo:
    if count<num:
        print(linha.rstrip('\n'))
        count += 1
    else:
        break

arquivo.close()