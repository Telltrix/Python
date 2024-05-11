class Automovel:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        self.marca= marca
        self.modelo= modelo
        self.ano= ano
        self.cor= cor
    
    def __str__(self):
        return f'Automóvel da marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}'
    
class Carro(Automovel):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, num_portas: int):
        super().__init__(marca, modelo, ano, cor)
        self.num_portas= num_portas
    
    def __str__(self):
        return f'Carro da marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, {self.num_portas} portas.'
    
carro_1= Carro('Ford', 'Fiesta', 2020, 'preto', 4)
print(carro_1.__str__)