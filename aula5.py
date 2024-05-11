# Tratando erros com try/except/else/finally
try: # Tenta executar todo codigo contido nele
    num1= int(input('Digite um número: '))
    num2= int(input('Digite outro número: '))
    resultado= num1/num2
except ValueError: # Caso ocorra um erro durante a execução do codigo contido no try ele entra e executa os codigos do except
    print('Valor informado não é um número')
except ZeroDivisionError: # Vários excepts podem ser tratados
    print('Valor não pode ser ZERO')
except Exception as error: # Quando você não saiba qual except pode ocorrer ou quer deixar mais genérico o feedback, dá pra usar o exception e dar um alias para ele exibir no feedback
    print(f'Algo deu errado: {error}')
else: # Executa caso o codigo no try não tenha exceções
    print('O resultado é:', resultado)
finally: # executa sempre ao final do try, mesmo ocorrendo exceções
    print('Fim da execução.')

# Tratando erro em Arrays
try:
    nomes= ['João', 'José', 'Jorge', 'James']
    indice= int(input('Qual indice quer acessar? '))
    aux= nomes[indice]
except IndexError:
    print(f'O indice {indice} não existe na lista!') # type: ignore
else:
    print(aux)
finally:
    print('Finalizando...')

# Praticando: Faça uma calculadora com as 4 operações básicas evitando as exceções

def adicao(num1, num2):
    resultado= num1+num2
    return resultado

def subtracao(num1, num2):
    resultado= num1-num2
    return resultado

def multiplicacao(num1, num2):
    resultado= num1*num2
    return resultado

def divisao(num1, num2):
    try:
        resultado= num1/num2
        return resultado
    except ZeroDivisionError:
        return 'Não pode dividir por zero!'
    
quebra= True
while quebra:
    try:
        numero1= float(input('Digite o primeiro numero:'))
        numero2= float(input('Digite o segundo numero: '))
    except ValueError:
        print('Digite apenas numeros')
    else:
        try:
            opcao= int(input('Escolha a operação que deseja executar com os numeros:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Desligar\n'))
        except ValueError:
            print('Digite apenas numeros')
        else:
            try:
                match opcao:
                    case 1:
                        print(adicao(numero1, numero2))
                    case 2:
                        print(subtracao(numero1, numero2))
                    case 3:
                     print(multiplicacao(numero1, numero2))
                    case 4:
                        print(divisao(numero1, numero2))
                    case 5:
                        print('Encerrando aplicação...')
                        quebra= False
                    case _:
                        raise ValueError('Opção inválida')
            except ValueError as erro:
                print('Erro ocorreu:', erro)

# Classes e objetos
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome= nome    # Atributo publico
        self._idade= idade # Atributo privado com _ na frente
        self.altura= altura
        self.vivo= True

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self._idade}\nAltura: {self.altura}'
    
    def andar(self, distancia):
        print(f'Sai para caminhar {distancia} metros')
    
    def set_idade(self, idade):
        self._idade= idade
    def get_idade(self):
        return self._idade
    
objeto_pessoa_1 = Pessoa('Telmo', 41, 1.84)
# objeto_pessoa_1.andar(100)
# print(objeto_pessoa_1)
# print(objeto_pessoa_1.nome)

# Encapsulamento - getter e setter
print(objeto_pessoa_1.get_idade())
objeto_pessoa_1.set_idade(input('Digite idade: '))
print(objeto_pessoa_1.get_idade())

# Praticar
class ContaBancaria:
    def __init__(self, numeroConta: int, senha: str):
        self.numero= numeroConta
        self._saldo= 0
        self._senha= senha

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, valor):
        self._saldo= valor
        return self.get_saldo()
    
    def __str__(self):
        return f'Conta numero: {self.numero}\nSaldo: {self._saldo}'
    
    def depositar(self, valor):
        self._saldo= self._saldo+valor
        return self.get_saldo()
    
    def sacar(self, valor):
        self._saldo= self._saldo-valor
        return self.get_saldo()

    
    
objeto_contaBancaria_1 = ContaBancaria(123, 321)
print(objeto_contaBancaria_1.depositar(500))
print(objeto_contaBancaria_1.sacar(200))
print(objeto_contaBancaria_1.get_saldo())
print(objeto_contaBancaria_1.set_saldo(5000))