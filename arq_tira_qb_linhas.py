meuArquivo = open('bandas.txt', 'r')
bandas = meuArquivo.readlines()

for banda in bandas:
    banda = banda.rstrip('\n')
    print(banda)

meuArquivo.close()