def piramide(n):
    for c in range(1, n + 1):
        letra = str(c)
        print(c * letra)

numero = int(input('Digite um número para imprimir:'))
piramide(numero)