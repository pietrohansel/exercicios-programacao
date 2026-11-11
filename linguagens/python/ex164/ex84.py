class ContaBancaria:
    '''
    Cria uma conta bancária e permite fazer saques e depósitos
    '''

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta criado com sucesso!')

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} "

    def deposito(self,valor):
        self.saldo += valor
        print(f'Deposito autorizado no valor de R${valor:.2f}')

    def saque(self,valor):
        if valor > self.saldo:
            print("Saque negado")
        else:
            self.saldo -= valor
            print(f'Saque autorizado no valor de R${valor:.2f}')


c1 = ContaBancaria(id = 1, nome = 'Pietro', saldo=1000)
c1.deposito(500)
c1.saque(2000)

print(c1.__doc__)
print(c1)