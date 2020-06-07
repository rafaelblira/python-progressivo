import pprint

texto = 'Curso Python Progressivo'
contador = {}

for char in texto:
    contador.setdefault(char, 0)
    contador[char] += 1
    
pprint.pprint(contador)