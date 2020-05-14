fatorial = 1
while True:
    numero = int(input("Fatorial de: "))
    if numero !=0:
        for n in range(1, numero +1):
            fatorial *= n
        print(fatorial)
    else:
        break