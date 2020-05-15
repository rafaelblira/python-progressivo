cand1 = 0
cand2 = 0
cand3 = 0
eleitores = int(input('Digite a quantidade de eleitores: '))
print('Para votar no Candidato 1 digite [1]\nPara votar no Candidato 2 digite [2]\nPara votar no Candidato 3 digite [3]')
for cont in range(0, eleitores):
    voto = str(input('Digite seu voto: '))
    if voto == '1':
        cand1 += 1
    if voto == '2':
        cand2 += 1
    if voto == '3':
        cand3 += 1
print('O resultado foi: \nO Candidato 1 recebeu {} votos;\nO Candidato 2 recebeu {} votos;\nO Candidato 3 recebeu {} votos.'.format(cand1, cand2, cand3))
