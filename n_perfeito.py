def perfeito(n):
    soma = 0
    for val in range(1, n):
        if n % val == 0:
            soma += val
    if soma == n:
        return True
    else:
        return False

def exibe():
    n = int(input('Exibir números perfeitos até o número: '))
    for val in range(1,n+1):
        if(perfeito(val)):
            print(val)


while True:
    exibe()