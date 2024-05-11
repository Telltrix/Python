class ContaBancaria:
    def __init__(self, numeroConta, senha):
        self.numero= numeroConta
        self._saldo= 0
        self._senha= senha

    def __str__(self):
        return f'Conta numero: {self.numero}\nSaldo: {self._saldo}'
    
    def depositar(self, valor):
        self._saldo= self._saldo+valor
        return self.get_saldo()
    
    def sacar(self, valor):
        self= self._saldo-valor
        return self.get_saldo()

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, valor):
        self._saldo= valor
        return self.get_saldo()
    
objeto_contaBancaria_1 = ContaBancaria(123, 321)
print(objeto_contaBancaria_1.depositar(500))
print(objeto_contaBancaria_1.sacar(200))
print(objeto_contaBancaria_1.get_saldo())
print(objeto_contaBancaria_1.set_saldo(5000))