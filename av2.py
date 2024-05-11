class Automovel:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
           self.marca= marca
           self.modelo= modelo
           self.ano= ano
           self.cor=cor
           self._velocidade= 0
           self._ligado= False

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}'
    
    def set_ligado(self):
        if self.get_ligado:
            aux= 'ligado'
            aux2= 'desligar'
        else:
            aux= 'desligado'
            aux2= 'ligar'

        opcao= input(f'Veiculo está: {aux}, gostaria de {aux2}?\n1 - Sim\n2 - não\n')
        match opcao:
            case '1':
                if aux == 'ligado':
                    self._ligado= False
                    aux= aux2
                    print('Veiculo foi desligado')
                else:
                    self._ligado= True
                    aux2= aux
                    print('Veiculo foi ligado')
            case '2':
                print(f'Veiculo permanece {aux}')
            case _:
                print('opção inválida')

    def get_ligado(self):
        return self._ligado

    def get_velocidade(self):
        return self._velocidade
    
    def set_velocidade(self):
        try:
            opcao= int(input('Escolha opção que deseja:\n1 - Aumentar a velocidade\n2 - Reduzir a velocidade\n'))
            match opcao:
                case 1:
                    self._velocidade+= 1
                    print(f'Velocidade atual: {self.get_velocidade()}km')
                
                case 2:
                    if self.get_velocidade() == 0:
                        print('Carro já está parado!')
                    else:
                        self._velocidade-= 1
                        print(f'Velocidade atual: {self.get_velocidade()}km')
        except ValueError as erro:
            print('Erro ocorreu:', erro)
veiculo_1= Automovel('Ford', 'Ka', 2021, 'Branco')
print(veiculo_1)
veiculo_1.set_ligado()
veiculo_1.set_velocidade()

class Carro(Automovel):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, num_portas: int):
        super().__init__(marca, modelo, ano, cor)
        self.num_portas= num_portas
        self._portas= False

    def set_ligado(self):
        if self.get_portas:
            aux= 'abertas'
            aux2= 'fechar'
        else:
            aux= 'aberto'
            aux2= 'abrir'

        opcao= input(f'Veiculo está com as portas: {aux}, gostaria de {aux2}?\n1 - Sim\n2 - não\n')
        match opcao:
            case '1':
                if aux == 'abertas':
                    self._portas= False
                    aux= aux2
                    print('Veiculo foi fechado')
                else:
                    self._portas= True
                    aux2= aux
                    print('Veiculo foi aberto')
            case '2':
                aux= 'aberto'
                print(f'Veiculo permanece {aux}')
            case _:
                print('opção inválida')
    
    def get_portas(self):
        return self._portas

    def set_velocidade(self):
        try:
            opcao= int(input('Escolha opção que deseja:\n1 - Aumentar a velocidade\n2 - Reduzir a velocidade\n'))
            match opcao:
                case 1:
                    self._velocidade+= 5
                    print(f'Velocidade atual: {self.get_velocidade()}km')
                
                case 2:
                    if self.get_velocidade() == 0:
                        print('Carro já está parado!')
                    else:
                        self._velocidade-= 5
                        print(f'Velocidade atual: {self.get_velocidade()}km')
        except ValueError as erro:
            print('Erro ocorreu:', erro)

carro_1= Carro('Ford', 'Ka', 2021, 'Branco', 2)
print(carro_1)
carro_1.set_ligado()
carro_1.set_velocidade()

class Moto(Automovel):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, estilo):
        super().__init__(marca, modelo, ano, cor)
        self.estilo= estilo

    def empinar(self):
        return 'Empinando'

    def set_velocidade(self):
        try:
            opcao= int(input('Escolha opção que deseja:\n1 - Aumentar a velocidade\n2 - Reduzir a velocidade\n'))
            match opcao:
                case 1:
                    self._velocidade+= 2
                    print(f'Velocidade atual: {self.get_velocidade()}km')
                
                case 2:
                    if self.get_velocidade() == 0:
                        print('Moto já está parada!')
                    else:
                        self._velocidade-= 2
                        print(f'Velocidade atual: {self.get_velocidade()}km')
        except ValueError as erro:
            print('Erro ocorreu:', erro)
        
moto_1= Moto('Honda', 'CG 150', 2020, 'Vermelho', 'passeio')
print(moto_1)
print(f'Você está {moto_1.empinar()}')
moto_1.set_velocidade()

class Caminhonete(Automovel):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, carga: int):
        super().__init__(marca, modelo, ano, cor)
        self.carga= carga
        self._cargaMaxima= 50
    
    def set_carga(self):
        while True:
            try:
                opcao= input('Deseja carregar mais a caminhonete?\n1 - Sim\n2 - Não\n')
                match opcao:
                    case '1':
                        self.carga+= 5
                        print(f'Carga total da caminhonete: {self.get_carga()}')
                        if self.get_carga() >= 50:
                            print('Atingiu carga máxima!')
                            break
                    case '2':
                        print(f'Carga total da caminhonete: {self.get_carga()}')
                        break
            except ValueError as erro:
                print('Erro ocorreu:', erro)

    def get_carga(self):
        return self.carga

    def set_velocidade(self):
        try:
            opcao= int(input('Escolha opção que deseja:\n1 - Aumentar a velocidade\n2 - Reduzir a velocidade\n'))
            match opcao:
                case 1:
                    self._velocidade+= 3
                    print(f'Velocidade atual: {self.get_velocidade()}km')
                
                case 2:
                    if self.get_velocidade() == 0:
                        print('Caminhonete já está parada!')
                    else:
                        self._velocidade-= 3
                        print(f'Velocidade atual: {self.get_velocidade()}km')
        except ValueError as erro:
            print('Erro ocorreu:', erro)
caminhonete_1= Caminhonete('Chevrolet', 'F1000', 2020, 'Azul', 25)
print(caminhonete_1)
caminhonete_1.set_carga()
caminhonete_1.set_velocidade()