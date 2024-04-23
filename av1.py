# 1) Crie um algoritmo no qual seja digitado a distância percorrida em quilômetros, 
# o tipo do carro e informe ao final a média de consumo estimado de combustível. 
# Sabendo-se que um carro do tipo A faz 8km/litro, o carro do tipo B faz 12km/litro e o tipo C faz 9km/litro. 
# Caso seja fornecido um tipo de carro inválido (diferente de A, B ou C) o algoritmo deve mostrar uma mensagem 
# "Tipo de carro inválido!" e encerrar.

# distance= float(input('Digite a distância percorrida em KM: '))
# carType =input('Qual o tipo de carro?\nA:\nB:\nC: ')

# match carType.upper():
#     case "A":
#         consume= 8
#         media= distance/consume
#         print(f'Média de consumo estimado de combustível foi: {media:.2f}')
#     case "B":
#         consume= 12
#         media= distance/consume
#         print(f'Média de consumo estimado de combustível foi: {media:.2f}')
#     case "C":
#         consume= 9
#         media= distance/consume
#         print(f'Média de consumo estimado de combustível foi: {media:.2f}')
#     case _:
#         print('Tipo de carro inválido!')

# 2) Crie um programa que leia três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno. 
# Quando os três lados forem iguais trata-se de um triângulo equilátero, dois lados iguais é um triângulo isósceles 
# e os três lados diferentes é um triângulo escaleno.

# side1= float(input('Digite o valor do 1º lado do triângulo: '))
# side2= float(input('Digite o valor do 2º lado do triângulo: '))
# side3= float(input('Digite o valor do 3º lado do triângulo: '))

# if side1 == side2 and side2 == side3:
#     result= 'É um triângulo equilátero.'
# elif side1 != side2 and side1 != side3 and side2 != side3:
#     result= 'É um triângulo escaleno.'
# else:
#     result= 'É um triângulo isósceles.'
# print(result)

# 3) Desenvolva um programa no qual o usuário deve digitar o nome e a idade de 3
# pessoas. Ao final mostrar a média de idade delas e a maior idade dentre essas
# pessoas.

# name1= input('Digite o nome da primeira pessoa: ')
# age1= int(input('Digite a idade da primeira pessoa: '))
# name2= input('Digite o nome da segunda pessoa: ')
# age2= int(input('Digite a idade da segunda pessoa: '))
# name3= input('Digite o nome da terceira pessoa: ')
# age3= int(input('Digite a idade da terceira pessoa: '))
# media= (age1+age2+age3)/3

# if age1 >= age2 and age1 >= age3:
#     major= f'{name1} é mais velho, com {age1} anos'
# elif age2 >= age3:
#     major= f'{name2} é mais velho, com {age2} anos'
# else:
#     major= f'{name3} é mais velho, com {age3} anos'
# print(f'Média de idade é: {media:.2f}\n{major}')

# 4) Em um determinado e-commerce, o frete para produtos possui o valor fixo de
# R$12,50. A loja possui benefícios para assinantes em três categorias: 
# 1) Assinante Premium, ganha 20% de desconto e frete grátis 
# 2) Assinante Gold, ganha 20% de desconto mas paga frete 
# 3) Assinante Silver, ganha 10% de desconto mas paga frete. 
# 4) Não assinante, sem benefícios. 
# Faça um programa que solicite o valor da compra e a categoria de assinante (1, 2, 3 ou 4). 
# Mostrar na tela o valor da compra de acordo com a opção escolhida.

# frete= 12.5
# valorCompra= float(input('Digite o valor da compra: '))
# categoriaAssinante = input('Qual a categoria do assinante?\n1)Premium\n2)Gold\n3)Silver\n4)Não assinante: ')

# match categoriaAssinante:
#     case '1':
#         frete = 0
#         desconto = 0.8
#     case '2':
#         desconto = 0.8
#     case '3':
#         desconto = 0.9
#     case '4':
#         desconto = 1
#     case _:
#         desconto = 0
#         print('Opção inválida.')
# print(f'Valor total: R${(frete+valorCompra)*desconto:.2f}')