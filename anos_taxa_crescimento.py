pais_a = int(input("População do país A: "))
while pais_a < 0:
    pais_a = int(input("População do país A: "))
pcresc_a = float(input("Taxa de crescimento da cidade A: "))

pais_b = int(input("População do país B: "))
while pais_b < 0:
    pais_b = int(input("População do país B: "))
pcresc_b = float(input("Taxa de crescimento da cidade B: "))

ano = 0
pcresc_a /= 100
pcresc_b /= 100
while pais_a < pais_b: 
    pais_a = int((1+ pcresc_a) * pais_a)
    pais_b = int((1+ pcresc_b) * pais_b)
    ano += 1
    print('Ano %d:' % ano)
    print('O numero de anos para o país A ter a mesma população do país B é {}'.format(ano))
    print('A população do país A é {} e a população do país B é {}'.format(pais_a, pais_b))
print('ultrapassa no ano: ', ano)
        

    

