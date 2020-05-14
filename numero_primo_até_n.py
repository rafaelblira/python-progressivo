total = int(input('Digite o total da séria para ver os primos: '))
for num in range(2, total):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        print(num)
            


        
        


        
            
    
