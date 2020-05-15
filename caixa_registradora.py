#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

print('Lojas Tabajara')
soma = 0
dinheiro = 0
troco = 0
preco = 0
cont = 0
while True:
    preco = float(input('Produto {}: '.format(cont + 1)))
    cont = cont + 1
    soma += preco
    if preco == 0: 
        print('Total: ', soma)
        dinheiro = float(input('Dinheiro: '))
        troco = dinheiro - soma
        print('Troco: ', troco)
        cont = 0
        print('=-'*30)

