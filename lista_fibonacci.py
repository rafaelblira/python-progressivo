print('Sequência Fibonacci')

termos = int( input('Quantos termos? ') )
seq = []

for c in range(termos):
    if(c == 0 or c == 1):
        seq.append(c)
    else:
        seq.append( seq[c-1] + seq[c-2] )

print('\n', seq)