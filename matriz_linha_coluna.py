matriz = [ [0 for i in range(4)] for j in range(4)] #i é a linha e j a coluna
count=0

for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = count #preenche a matriz com números de count
        count += 1

for linha in range(4):
    for coluna in range(4):
        print("%4d" % matriz[linha][coluna], end='')
    print()