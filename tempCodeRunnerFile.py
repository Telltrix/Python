numero= int(input(f'Digite um numero acima de 1 para verificar se ele é primo: '))
if numero < 2:
    print('Numero digitado menor que 2!')
for count in range (1, numero+1):
    aux=2
    primo= True
    check= 0
    while aux < count:
        if count <= 1:
            primo= False
        else:    
            check= count%aux
        if check == 0:
            primo= False
        aux+= 1
    if primo and count > 1:
        print(f'{count} é primo')