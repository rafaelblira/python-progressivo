def alterahora(hora, minutos):
    if hora > 12:
        hora = hora - 12
        print(hora, ':', minutos, 'PM')
    else:
        print(hora, ':', minutos, 'AM')

while True:
    h = int(input('Digite a hora: '))
    m = int(input('Digite os minutos: '))
    alterahora(h, m)
