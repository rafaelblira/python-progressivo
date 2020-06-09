def eTelefone(numero):
    if len(numero) != 9:
        return False
    for index in range(0,4):
        if numero[index].isdecimal() is not True:
            return False  
    if numero[4] != '-':
        return False
    for index in range(5,9):
        if numero[index].isdecimal() is not True:
            return False
    print("Numero detectado: ", numero)
    return True
 
while True:
    numero = input("Numero no formato 'xxxx-yyyy': " )
 
    for i in range( len(numero)):
        pedaco=numero[i:i+9]
        eTelefone(pedaco)