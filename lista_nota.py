n = int(input("Numero de materias: "))
notas = []
soma=0

for count in range(n):
    nota=float(input("Nota da materia %2d: " % (count+1)))
    notas += [nota]    
    soma += nota

print("Notas: ",notas)
print("Media: %.2f" % (soma/n))