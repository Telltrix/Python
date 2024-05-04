# 1) Mostre uma contagem regressiva de 10 até 1 e após exiba a mensagem "Foguete lançaddo!"
numero= 10
for count in range (10):
    print(numero-count)
print('Foguete lançado!')

# 2) Mostre os números de 0 a 200 de 3 em 3
for count in range (3,200,3):
    print(count)

# 3) Faça um programa no qual o usuário deve digitar a sequência de números de 1 a 10,
# invertida. Caso digite algum número fora da sequência, interromper e mostrar uma
# mensagem "Você errou a sequência". Do contrário, ao final mostrar uma mensagem
# "Você terminou a sequência corretamente".
sequence=10
for count in range(10):
    number= int(input('Digite um numero na sequência de 10 até 1\n'))
    if number != sequence:
        resultado= 'Você errou a sequência'
        break
    else:
        sequence-= 1
        resultado= 'Você terminou a sequência corretamente'
print(resultado)

# 4) Desenvolver um programa no qual o usuário digite o número de multas que deseja cadastrar
# e para cada multa deve colocar o valor em reais e os pontos perdidos na carteira de habilitação.
# Ao final, mostrar o somatório das multas e dos pontos, caso os pontos alcancem 21 ou mais,
# exibir a mensagem “Você está irregular”, senão, exibir “Você está regular”.
quantidade= int(input('Digite a quantidade de multas a cadastrar: '))
pontos= 0
saldo= 0
for count in range (quantidade):
    saldo= float(input(f'Digite o valor da {count+1}º multa: '))+saldo
    pontos= int(input(f'Digite a quantidade de pontos da {count+1}º multa: '))+pontos
if pontos >= 21:
    result= f'Valor total das multas: R${saldo:,.2f}\nVocê está irregular com {pontos} pontos'
else:
    result= f'Valor total das multas: R${saldo:,.2f}\nVocê está regular com {pontos} pontos'
print(result)

# 5) Criar um jogo de adivinhação. O usuário deve digitar um número entre 0 e 100 (número
# secreto). Em seguida deve ser perguntado qual número imagina-se que seja o número secreto.
# A cada rodada, deve-se dar dicas após o palpite "o número digitado é menor" ou "o número
# digitado é maior". Quando o número for adivinhado, mostrar uma mensagem de
# parabéns e o número de tentativas realizadas.
secret= float(input('Digite um numero de 0 à 100: '))
guess= -1
tryes= 0
while guess != secret:
    tryes+=1
    guess= float(input('Digite um numero: '))
    if guess > secret:
        print(f'Numero secreto é menor que: {guess}')
    elif guess < secret:
        print(f'Numero secreto é maior que: {guess}')
print(f'Parabéns vcê adivinhou o numero secreto em após {tryes} tentativas')

# 6) O acampamento base sul do Everest fica a cerca de 5.360m de altura. A partir dele, muitas expedições
# partem rumo ao cume que fica a 8.848m de altura, levando dias para chegar. Considerando a saída do
# acampamento base, faça um programa que pergunte ao usuário a altitude em metros escalada no dia.
# Caso seja atingida a marca de 8 dias e não tenha chegado ao cume, mostrar mensagem “Você deve
# voltar, pois corre risco de ficar sem oxigênio”. Se chegar ao cume em menos de 8 dias, mostrar a
# quantidade de dias que foram necessários para tal.
altitudeBase= 5360
cume= 8848
count=0
while altitudeBase < cume:
    count+= 1
    altitudeBase= int(input(f'Digite quantos metros escalou no {count}º dia: '))+altitudeBase
    print(f'Altura total escalada até o momento: {altitudeBase}')
    if count == 9:
        result= 'Você deve voltar, pois corre risco de ficar sem oxigênio'
        break
    else:
        result= f'Você chegou no topo em {count} dias'
print(result)

# 7) Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
# crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de
# 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
populacaoA= 80000
populacaoB= 200000
taxaA= 0.03
taxaB= 0.015
ano= 0
while populacaoA < populacaoB:
    populacaoA = populacaoA+(populacaoA*taxaA)
    populacaoB = populacaoB+(populacaoB*taxaB)
    ano+=1
print(f'O pais A levou {ano} anos para ultrapassar o pais B em população.')

# 8) Os números primos possuem várias aplicações dentro da Computação, por exemplo, na criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça ao usuário para digitar cinco números inteiros e mostre na tela se são
# primos ou não.
for count in range (5):
    aux=2
    primo= 'É primo!'
    numero= int(input(f'Digite {count+1}º numero acima de 1 para verificar se ele é primo: '))
    if numero <= 1:
        print(f'{numero} não é primo')
        break
    while aux < numero:
        check= numero%aux
        if check == 0:
            primo= 'Não é primo!'
        aux+= 1
    print(f'{numero} {primo}')

# 9) Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
# digitado pelo usuário.
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

# 10) Você é um colecionador de vinis e resolveu ir ao sebo para comprar alguns vinis raros. Porém, você
# tem apenas R$200 para gastar. Faça um programa que pergunte o nome do vinil e o
# valor, repetidamente. Caso o valor ultrapasse R$200, encerrar (desconsiderando o último vinil). Mostrar na tela:
# Total gasto em reais
# Valor que sobrou
# Quantos foram comprados
# A média de preço
# O mais caro e o mais barato
# saldo=200
