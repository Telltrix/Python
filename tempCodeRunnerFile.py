aux=1
for count in range(5):
    numero= int(input(f'Digite o {count+1}º numero: '))
    while aux <= numero:
        check= numero%aux
        if check == 0:
            primo= f'{numero} é primo!'
            aux+= 1
        else:
            primo= f'{numero} não é primo!'
            break
    print(primo)