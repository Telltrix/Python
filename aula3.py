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

def somar(number1, number2):
    return number1+number2

def subtrair(number1, number2):
    return number1-number2

def multiplicar(number1, number2):
    return number1*number2

def dividir(number1, number2):
    return round(number1/number2,2)

def calculator(number1, number2):
    operacao = input('Qual a operação entre os numeros quer realizar?\nDigite 1 para Adição\nDigite 2 para Subtração\nDigite 3 para Multiplicação\nDigite 4 para Divisão\n ')
    match operacao:
        case '1':
            return somar(number1, number2)
        case '2':
            return subtrair(number1, number2)
        case '3':
            return multiplicar(number1, number2)
        case '4':
            return dividir(number1, number2)
        case _:
            return 'Opção inválida!'

print(f'Resultado: {calculator(float(input('Digite o primeiro numero: ')), float(input('Digite o segundo numero: ')))}')