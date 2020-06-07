notas={'João'   :  9,
       'Maria'  : 10,
       'José'   : 4  }

nome = input("Aluno a mudar a nota: ")
nota = float(input("Nova nota     : "))

if nome in notas.keys():
    notas[nome] = nota
else:
    print("Não existe esse aluno")
print(notas)