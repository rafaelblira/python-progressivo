numero = int(input("Fatorial de: "))
fatorial = 1
while numero != 0:
    for n in range(1, numero +1):
        fatorial *= n
    print(fatorial)
    break