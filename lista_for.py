numeros = []

for count in range(10):
    numeros += [count]

soma=0
for count in numeros:
    print(count, '!')
    soma += count

print("Soma: ", soma)