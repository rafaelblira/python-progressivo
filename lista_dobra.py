numeros = []

for count in range(1,11):
    numeros += [count]

for count in range(len(numeros)):
    numeros[count] = numeros[count]*2
    
for count in numeros:
    print(count)