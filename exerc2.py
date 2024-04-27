# 1) Crie um programa que peça para o usuário digitar três notas individualmente
# (uma por vez), faça a média e caso a média seja igual ou maior que 7, mostre
# uma mensagem "Aprovado!" e a média. Caso seja menor que 7, mostre uma mensagem
# "Reprovado!" e a média.

# nota1= float(input('Digite a primeira nota: '))
# nota2= float(input('Digite a segunda nota: '))
# nota3= float(input('Digite a terceira nota: '))
# media= float((nota1+nota2+nota3)/3)
# if media >= 7 and media <= 10:
#     resultado= f'Aprovado, média: {media:.2f}'
# elif media >= 0 and media < 7:
#     resultado= f'Reprovado, média: {media:.2f}'
# else:
#     resultado= 'Média incoerente, reveja as notas inseridas'
# print(resultado)

# 2) Faça um programa para ler o salário anual de um funcionário e o piso
# salarial mensal da sua categoria. Mostrar o salário mensal do funcionário e
# dizer se ele recebe de acordo com o piso (salário mensal igual ou maior que o
# piso da categoria) ou se recebe abaixo do piso.

# soldo_anual= float(input('Digite sue salário anual: '))
# piso_categoria= float(input('Digite o piso da sua categoria: '))
# salario_mensal= float(soldo_anual/12)
# if salario_mensal >= piso_categoria:
#     result= f'Salário mensal igual ou superior que o piso da categoria!'
# else:
#     result= f'Salário mensal abaixo do piso da categoria!'
# print(f'{result}. Salário mensal de:{salario_mensal:.2f}')

# 3) Criar um programa que pergunte o nome e a idade da pessoa, e se tem
# comorbidade (S ou N). Mostrar mensagem "Pode se vacinar!" caso a idade seja
# maior ou igual a 60 ou tenha comorbidade. Caso contrário, mostrar mensagem "Não
# pode se vacinar!".

# name= input('Digite seu nome: ')
# age= int(input('Digite sua idade: '))
# comorb= input('Digite S se tem comorbidade ou N caso não tenha: ')

# if age >= 60 or comorb == 'S' or comorb == 's':
#     print("Pode se vacinar!")
# else:
#     print("Não pode se vacinar!")

# 4) Fazer um programa no qual o usuário digite a sua altura e o seu peso, ao
# final mostre o IMC (índice de massa corporal) e uma mensagem se está abaixo do
# peso (IMC menor que 18), na faixa de peso ideal (IMC de 18 a 25) ou acima do
# peso (IMC maior 25). IMC = peso / (altura * altura).

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# IMC= float(peso/(altura*altura))

# if IMC >= 18 and IMC <= 25:
#     print(f'Seu IMC é: {round(IMC, 2)} e esta na faixa de peso ideal.')
# elif IMC < 18:
#     print(f'Seu IMC é: {IMC:.2f} e está abaixo do peso ideal.')
# else:
#     print(f'Seu IMC é: {IMC:.2f} e está acima do peso ideal.')

# 5) Criar um programa que simule o login de um roteador. O nome de usuário
# (username) é "admin" e a senha (password) "123". Pedir ao usuário para digitar
# username e password. Caso os dados estejam corretos, mostrar uma mensagem
# "Login efetuado!", caso contrário "Login falhou!". (DESAFIO: Mostrar mensagens
# específicas para erro de username, de password ou de ambos).

# username= input('Digite o login: ')
# password= input('Digite a senha: ')

# if (username.lower() == 'admin') and password == '123':
#     print("Login efetuado!")
# elif (username.lower() != 'admin'):
#     print('Login inválido!')
# elif (username.lower() == 'admin') and password != '123':
#     print("Password incorreto!")

# 6) Elaborar um programa que alerte sobre os riscos de animais em extinção. O
# usuário deve digitar o nome da espécie e a sua população (total de indivíduos).
# Populações entre 0 e 500 indivíduos, são classificadas como "Espécie
# criticamente em perigo", populações entre 501 e 1000 indivíduos, são
# classificadas como "Espécie em perigo" e populações entre 1001 e 5000
# indivíduos, são classificadas como "Espécie vulnerável!"

# especie= input('Digite o nome da espécie do animal: ')
# populacao= int(input('Digite quantidade de animais: '))

# if populacao < 501 and populacao >= 0:
#     mensagem= 'Espécie criticamente em perigo!'
# elif populacao > 500 and populacao  < 1001:
#     mensagem= 'Espécie em perigo'
# elif populacao > 1000 and populacao < 5001:
#     mensagem= 'Espécie vulnerável'
# else:
#     mensagem= 'Espéciel fora de perigo'
# print(f'{especie}: {mensagem}')

# 7) Criar um programa para calcular a densidade demográfica (habitantes por
# quilômetro quadrado) de uma região. Sendo, densidade igual a população (total
# de habitantes) dividida pela área (metros quadrados). Mostrar mensagens para
# densidade alta (maior que 100), média (entre 25 e 100), baixa (menor que 25).

# habitantes= int(input('Digite a quantidade de habitantes: '))
# area= float(input('Digite a area em m²: '))
# densidade= habitantes/area

# if densidade >= 25 and densidade <= 100:
#     mensagem= f'Densidade média. {densidade:.2f}'
# elif densidade > 100:
#     mensagem= f'Densidade alta. {densidade:.2f}'
# elif densidade < 25 and densidade >= 0:
#     mensagem= f'Densidade baixa. {densidade:.2f}'
# else:
#     mensagem= 'Densidade incoerente.'
# print(mensagem)

# 8) Pedir 2 números para o usuário e mostrar qual é o maior e qual é o menor ou
# se são iguais.
# Exemplo: 70 é maior que 23
# Exemplo: 52 é igual a 52

# number1= float(input('Digite um numero: '))
# number2= float(input('Digite um segundo numero: '))

# if number1 == number2:
#     print(f'{number1:.2f} é igual à {number2:.2f}')
# elif number1 > number2:
#     print(f'{number1:.2f} é maior que {number2:.2f}')
# else:
#     print(f'{number2:.2f} é maior que {number1:.2f}')

# 9) Pedir para o usuário digitar 1 numero, mostrar se é par ou impar e se é
# positivo ou negativo.
# number= int(input('Digite um numero: '))
# estado= number%2

# if estado == 0:
#     parImpar = 'par'
# else:
#     parImpar = 'impar'
# if number >= 0:
#     posNeg= 'positivo'
# else:
#     posNeg= 'negativo'
# print(f'Numero: {number} é {parImpar} e {posNeg}')

# 10) Desenvolva um programa no qual o usuário deve digitar o nome e a idade de 3
# pessoas. Ao final mostrar a média de idade delas e a maior idade dentre essas
# pessoas.

# name1= input('Digite o nome da primeira pessoa: ')
# age1= int(input('Digite a idade da primeira pessoa: '))
# name2= input('Digite o nome da segunda pessoa: ')
# age2= int(input('Digite a idade da segunda pessoa: '))
# name3= input('Digite o nome da terceira pessoa: ')
# age3= int(input('Digite a idade da terceira pessoa: '))
# media= age1+age2+age3/3

# if age1 >= age2 and age1 >= age3:
#     major= f'{name1} é mais velho, com {age1} anos'
# elif age2 >= age3:
#     major= f'{name2} é mais velho, com {age2} anos'
# else:
#     major= f'{name3} é mais velho, com {age3} anos'
# print(f'Média de idade é: {media:.2f}\n{major}')

# 11) Criar um programa que informa quantos dias tem determinado mês
# (desconsiderando ano bissexto) do ano. Deve ser perguntado ao usuário o mês e a
# resposta deve ser numérica. Exemplo: Usuário digitou 3, que corresponde a
# março. Mostrar na tela "O mês possui 31 dias".

# mes= int(input('Digite o numero correspondente ao mês: '))

# match mes:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print('31 dias')
#     case 2:
#         print('28 dias')
#     case 4 | 6 | 9 | 11:
#         print('30 dias')
#     case _:
#         print('Mês inválido')

# 12) Desenvolva um programa que pergunte ao usuário o número da sua conta bancária e o tipo de 
# operação a ser realizada: 1) Saldo 2) Depósito 3) Saque. Nas opções de depósito e saque, perguntar 
# o valor a ser depositado ou sacado e mostrar o saldo atualizado na tela. Na opção saldo, apenas mostrar 
# o saldo atual na tela. Considere que um saque só pode ser realizado caso haja saldo suficiente. 
# Criar uma variável com um valor que represente o saldo inicial.

# saldo = 1000
# opcao_desejada = int(input('Qual operação você deseja realizar?\n1)Saldo\n2)Depósito\n3)Saque: '))

# match opcao_desejada:
#     case 1:
#         print(f'Seu saldo é de R${saldo}')
#     case 2:
#         deposito = float(input('Digite o valor do depósito: '))
#         if deposito > 0:
#             saldo = saldo + deposito
#             print(f'Seu saldo é de R${saldo}')
#         else:
#             print('Valor de depósito inválido.')
#     case 3:
#         saque = float(input('Digite o valor do saque: '))
#         if saque <= saldo and saque > 0:
#             saldo = saldo - saque
#             print(f'Seu saldo é de R${saldo}')
#         else:
#             print('Valor de saque inválido.')
#     case _:
#         print('Opção inválida.')

# 13) Em um determinado e-commerce, o frete para produtos possui o valor fixo de
# R$12,50. A loja possui benefícios para assinantes em três categorias: 
# 1) Assinante Premium, ganha 20% de desconto e frete grátis 
# 2) Assinante Gold, ganha 20% de desconto mas paga frete 
# 3) Assinante Silver, ganha 10% de desconto mas paga frete. 
# 4) Não assinante, sem benefícios. 
# Faça um programa que solicite o valor da compra e a categoria de assinante (1, 2, 3 ou 4). 
# Mostrar na tela o valor da compra de acordo com a opção escolhida.

frete= 12.5
valorCompra= float(input('Digite o valor da compra: '))
categoriaAssinante = input('Qual a categoria do assinante?\nDigite 1 para clientes Premium\nDigite 2 para clientes Gold\nDigite 3 para clientes Silver\nDigite 4 para clientes Não assinante\n ')

match categoriaAssinante:
    case '1':
        frete = 0
        desconto = 0.8
        print(f'Valor total: R${frete+(valorCompra*desconto):.2f}')
    case '2':
        desconto = 0.8
        print(f'Valor total: R${frete+(valorCompra*desconto):.2f}')
    case '3':
        desconto = 0.9
        print(f'Valor total: R${frete+(valorCompra*desconto):.2f}')
    case '4':
        desconto = 1
        print(f'Valor total: R${frete+(valorCompra*desconto):.2f}')
    case _:
        desconto= 0
        print('Opção inválida.')

# 14) Numa competição de arremesso de peteca, o competidor tem direito a 3
# arremessos para que a peteca caia em um alvo com áreas e pontuações de 0 a 5,
# sendo 5 no centro e 0 fora do alvo. Faça um programa que pergunte a pontuação de
# cada arremesso e ao final mostre o resultado (soma dos pontos) e a classifição:
# 15 pontos (deus da peteca), de 14 a 10 (petequeiro profissa), de 9 a 5 (petequeiro
# de final de semana), de 4 a 1 (pseudo-petequeiro) e 0 pontos (nunca petequeiro).

# arremesso= int(input('Digite a quantidade de arremesso do participante: '))
# total=0
# x= int(0)
# while x < arremesso:
#   x += 1
#   pontuacao= int(input(f'Digite a pontuação do {x}º arremesso: '))
#   total=total+pontuacao
#   print(f'Total parcial: {total}')
# if total >= 15:
#   print(f'{total} pontos: Deus da peteca!')
# elif total < 15 and total >= 10:
#   print(f'{total} pontos: Petequeiro profissional!')
# elif total < 10 and total >= 5:
#   print(f'{total} pontos: Petequeiro de final de semana!')
# elif total < 5 and total >= 1:
#   print(f'{total} pontos: Petequeiro de final de semana!')
# else:
#   print(f'{total} pontos: Nunca Petequeiro!')