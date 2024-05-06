def listarSabores():
    sabores= ['Morango', 'Manga', 'Uva']
    opcao= input(f'Digite o valor correspondente ao sabor:\n1- {sabores[0]}\n2- {sabores[1]}\n3- {sabores[2]}\n')
    match opcao:
        case '1':
            return sabores[0]
        case '2':
            return sabores[1]
        case '3':
            return sabores[2]
        case _:
            print('Valor incorreto.')
def listarSorvete(sorvete):
    if len(sorvete) == 0:
        print('Seu sorvete não possui sabores!')
    for count in range(len(sorvete)):
        print(f'{count+1}º camada, sabor: {sorvete[count]}')
sorvete=[]
quebra = True
while quebra:
    menu= input(f'Menu da sorveteria digite o valor correspondente a opção:\n1- Adicionar sabor\n2- Remover sabor\n3- Vizualizar sorvete\n4- Finalizar o pedido\n')
    match menu:
        case '1':
            if len(sorvete) == 4:
                print('Limite de sabores atingido, remova um sabor!')
            else:
                sorvete.append(listarSabores())
                print('Sabor adicionado!')
        case '2':
            if len(sorvete) == 0:
                print('Não existem sabores adicionados!')
            else:
                sorvete.pop()
                print('Sabor removido!')
        case '3':
            listarSorvete(sorvete)
        case '4':
            if len(sorvete) == 0:
                print('Adicione pelo menos um sabor!')
            else:
                print('Pedido realizado!')
                quebra = False
        case _:
            print('Valor incorreto')