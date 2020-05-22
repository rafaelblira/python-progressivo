#A série de Fibonacci é uma sequência de números, cujos dois primeiros são 0 e 1. O termo seguinte da sequência é obtido somando os dois anteriores. Faça uma script em Python que solicite um inteiro positivo ao usuário, n. Então uma função exibe todos os termos da sequência até o n-ésimo termo. Use recursividade.
print('Sequência Fibonacci')
def fibo(n):
   
    if n ==1:
       return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def menu():
    n = int(input('Exibir ate o termo (maior que 2): '))

    for val in range (1, n + 1):
        print (fibo(val), end=' ')
        

while True:
    menu()
    
 