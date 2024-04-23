.5
valuePurchase= float(input('Digite o valor da compra: '))
category = input('Qual a categoria do assinante?\n1)Premium\n2)Gold\n3)Silver\n4)Não assinante: ')

match category:
    case '1':
        freight = 0
        discount = 0.8
        print(f'Valor total: R${freight+(valuePurchase*discount):.2f}')
    case '2':
        discount = 0.8
        print(f'Valor total: R${freight+(valuePurchase*discount):.2f}')
    case '3':
        discount = 0.9
        print(f'Valor total: R${freight+(valuePurchase*discount):.2f}')
    case '4':
        discount = 1
        print(f'Valor total: R${freight+(valuePurchase*discount):.2f}')
    case _:
        print('Opç