total = int(input('Digite o total da séria para ver os primos: '))
cont = 0
for num in range(2, total + 1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        cont += 1
        print(num)
print('A seqência possui {} números primos'.format(cont))
            


        
        


        
            
    
