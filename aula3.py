#funções
# def showNameAge(name, age):
#     print(f'Nome: {name}\nIdade: {age} anos')

# showNameAge(input('Digite nome: '), input('Digite idade: '))

# def verificarNivelDano(dano):
#     if dano > 10:
#         print('Dano critico!')
#     else:
#         print('Dano normal.')

# verificarNivelDano(5)
# verificarNivelDano(10)
# verificarNivelDano(11)

# def somar(numero1, numero2):
#     return numero1+numero2

# print(f'Soma é: {somar(3, 5)}')

# def exponentiation(number, exponent):
#     return number**exponent
# print(f'Resultado: {exponentiation(int(input('Digite o numero: ')), int(input('Digite o exponenciador: ')))}')

# def parImpar(number):
#     if number % 2 == 0:
#         parImpar = 'par'
#     else:
#         parImpar = 'impar'
#     print(f'Numero: {number} é {parImpar}')
# parImpar(int(input('Digite um numero: ')))

# def somar(number1, number2):
#     return number1+number2

# def subtrair(number1, number2):
#     return number1-number2

# def multiplicar(number1, number2):
#     return number1*number2

# def dividir(number1, number2):
#     return round(number1/number2,2)

# def calculator(number1, number2):
#     operacao = input('Qual a operação entre os numeros quer realizar?\nDigite 1 para Adição\nDigite 2 para Subtração\nDigite 3 para Multiplicação\nDigite 4 para Divisão\n ')
#     match operacao:
#         case '1':
#             return somar(number1, number2)
#         case '2':
#             return subtrair(number1, number2)
#         case '3':
#             return multiplicar(number1, number2)
#         case '4':
#             return dividir(number1, number2)
#         case _:
#             return 'Opção inválida!'
# print(f'Resultado: {calculator(float(input('Digite o primeiro numero: ')), float(input('Digite o segundo numero: ')))}')

# def calcularPrecoTerreno(largura, comprimento):
#     precoMetro= float(1000)
#     return (largura*comprimento)*precoMetro
# print(f'Estimativa do valor do terreno de 50x20 é: R${calcularPrecoTerreno(50, 20):,.2f}')
# print(f'Estimativa do valor do terreno de 100x400 é: R${calcularPrecoTerreno(100, 400):,.2f}')
# print(f'Estimativa do valor do terreno de 20x1000 é: R${calcularPrecoTerreno(20, 1000):,.2f}')

# count= 0
# while count < 10:
#     count += 1
#     print(f'Contador vale: {count}')

# count= 0
# while count < 10:
#     count += 1
#     if (count % 3) == 0:
#         continue
#     print(count)

# soma= 0
# while soma <= 100:
#     numero= int(input('Digite um numero: '))
#     soma += numero
#     print(f'Valor atual da soma: {soma}')
# print(f'Valor da soma final: {soma}')

# for count in range(5):
#     print(count)
#     nome= input('Digite nome: ')
#     if count == 3:
#         break
#     print(nome)

#o range começa em i, ate x somando y(i, x, y)
# for count in range(2, 10, 3):
#     print(count)

# soma= 0
# quantidade= int(input('Digite quantidade de notas a ser informada: '))
# for count in range(quantidade):
#     soma= int(input(f'Digite {count+1}º nota: '))+soma
# print(f'Média das notas é: {soma/quantidade:.2f}')

# nomes=[]
# for count in range(3):
#     nomes.append(input('Digite nome: '))
#     print(f'Nome: {nomes[count]} esta na posição: {count} da lista')