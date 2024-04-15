# 1) Crie um programa que peça os dados de um cliente: Nome, idade, nacionalidade, endereço. Após digitados os dados, mostrar na tela a seguinte mensagem 
# "Cliente [Nome], com [idade] anos, [nacionalidade], reside no endereço [endereço]". Exemplo: Cliente Lucas, com 29 anos, brasileiro, reside no endereço Rua Victor Meirelles, 281, Centro, Florianópolis.

# name = input('Digite seu nome: ')
# age = int(input('Digite quantos anos você tem: '))
# nacionality = input('Digite sua nacionalidade: ')
# address = input('Digite seu endereço: ')
# print(f'Cliente {name}, com {age} anos, {nacionality}, reside no endereço: {address}.')

# 2) Faça um programa no qual o usuário digite dois números e mostre na tela a multiplicação desses números.

# number1 = float(input('Digite um numero: '))
# number2 = float(input('Digite outro numero: '))
# print(number1*number2)

# 3) Você é um amante da natureza e adora fazer trilhas. Criar um programa que calcule a velocidade média das trilhas que você realiza. Para isso, devem ser digitados
# os dados de distância percorrida (quilômetros) e tempo que a trilha durou (horas). Fazer então o cálculo da velocidade média e mostrar na tela a mensagem
# "Sua média de velocidade durante essa trilha foi de X km/h", sendo X a velocidade. 

# distance = float(input('Digite a distancia percorrida em quilometros: '))
# time = int(input('Digite quantas horas a trilha durou: '))
# print(f'Sua média de velocidade durante essa trilha foi de {distance/time}km/h.')

# 4) Na sua lista de compras do mercado, constam apenas 3 itens: arroz, batata palha e um suco de garrafa. Porém, você possui apenas uma nota de R$100 para pagar. 
# Faça um programa no qual sejam digitados os valores dos itens e mostre na tela valor que você deve receber (troco).

# rice = float(input('Digite o valor do arroz: '))
# potato = float(input('Digite o valor da batata palha: '))
# juice = float(input('Digite o valor do suco de garrafa: '))
# print(f'Seu troco é de: R${100-(rice+potato+juice)}')

# 5) Uma feira de livros está fazendo promoção onde na compra de 3 livros, o(a) comprador(a) ganha 15% de desconto. Criar um programa que receba os valores dos 3 livros
# e mostra na tela o total dos livros sem desconto e com desconto.

# book1 = int(input('Digite o valor do primeiro livro: '))
# book2 = int(input('Digite o valor do secundo livro: '))
# book3 = int(input('Digite o valor do terceiro livro: '))
# total = book1+book2+book3
# print(f'Valor total sem desconto é: R${total}\n Valor total com desconto: R${(total-(total*0.15))}')

# 6) Uma cidade pretende apurar os votos de sua eleição. Faça um programa para ler o número total de eleitores. Em seguida o número de votos do candidato X, 
# o número de votos do candidato Y, total de votos brancos e total de votos nulos (a soma desses quatro, deve ser igual ao total de eleitores). 
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

# electors = int(input('Digite o numero total de eleitores: '))
# candX = int(input('Digite a quantidade de votos do candidato X: '))
# candY = int(input('Digite a quantidade de votos do candidato Y: '))
# blank = int(input('Digite a quantidade de votos em branco: '))
# nulls = int(input('Digite a quantidade de votos nulos: '))
# tot = candX+candY+blank+nulls

# if(tot!=electors):
#     print(f'Quantidade de votos apurados({tot}) esta discrepante com a quantidade de eleitores({electors})')
# else:
#     print(f'O candidato X teve {(candX/tot)*100}% dos votos.')
#     print(f'O candidato Y teve {(candY/tot)*100}% dos votos.')
#     print(f'Votos em branco foram {(blank/tot)*100}% dos votos.')
#     print(f'Votos anulados foram {(nulls/tot)*100}% dos votos.')

# 7) Crie um programa no qual o usuário deve digitar um número (base) e o seu expoente. Apresentar na tela o resultado da exponenciação.

# numBase = int(input('Digite o numero base: '))
# numExpo = int(input('Digite o expoente: '))
# print(numBase**numExpo)

# 8) Uma pousada cobra R$280 reais a diária por quarto e R$15 reais o café por pessoa por dia. Você pretende passar um tempo com alguns amigos nessa pousada, 
# sendo que todos ficarão no mesmo quarto. Informar a quantidade de pessoas, o número de diárias e quantas pessoas do grupo vão querer café diário. Mostrar na tela o total a pagar.

# people = int(input('Digite quantidade de pessoas: '))
# diary = int(input('Digite a quantidade de diarias: '))
# cooffe = int(input('Digite quantodade de pessoas que vão querer o café diário: '))
# print(f'Total a pagar: R${(280*diary)+(cooffe*15)}')

# 9) Criar um programa que realize o cálculo de uma média da faculdade. A média é composta por três notas: Atividade Individual (peso 1), Seminário em Equipe (peso 1), Projeto final (peso 3).
# O usuário deve digitar as três notas e a média deve ser mostrada na tela.

# ind = float(input('Digite a nota da atividade individual: '))
# semi = float(input('Digite a nota do seminário em equipe: '))
# final = float(input('Digite a nota do projeto final: '))
# final = final*3
# print(f'A média do aluno é; {(ind+semi+final)/5}')

# 10) Criar um programa que calcule o IMC, no qual o usuário deve digitar o seu peso e altura, realizar o cálculo (peso / altura * altura) e mostrar o resultado na tela, 
# com 3 casas depois da vírgula.

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# print(f'Seu IMC é: {peso/(altura*altura)}')

# 11) Em uma fábrica de reciclagem de materiais, cada 10kg de plástico rendem R$2,00 cada 30kg de papel rendem R$3,00 e cada 50kg de metal rendem R$5,00. 
# Perguntar ao usuário a quantidade (kg) de cada material que deseja entregar na fábrica e mostrar o total que receberá em reais.

# plast = int(input('Digite a quantidade em kilos de plastico entregue: '))
# paper = int(input('Digite a quantidade em kilos de papel entregue: '))
# metal = int(input('Digite a quantidade em kilos de metal entregue: '))
# plast = (plast//10)*2
# paper = (paper//30)*3
# metal = (metal//50)*5
# print(f'Total entregue: R${plast+paper+metal}')

# 12) Em uma festa de família alemã, 45 pessoas foram convidadas para beber. Para tanto, foram comprados 300 litros de chopp. 
# Criar um programa que calcule a média de litros bebidos por pessoa, considerando ainda a quantidade de chopp (litros) desperdiçado e a quantidade de chopp (litros) que sobrou. 
# Esses dados devem ser digitados pelo usuário. Caso não tenha havido desperdício e não tenha sobrado chopp, digitar 0 para ambos. Ao final, mostrar a média de litros bebidos por 
# pessoa na festa.

# choppSobra = float(input('Digite a quantidade de chopp em litros que sobrou: '))
# choppDesper = float(input('Digite a quantidade de chopp em litros que foi desperdiçado: '))
# print(f'Média de chopp bebido por pessoa foi de: {(300-choppSobra+choppDesper)/45} litros')