#Herdar classe

class ContaBancaria():
    def __init__(self, numero_conta, saldo = 0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor 
        self.registrar_transacoes = ("Deposito", valor)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacoes = ("Saque", valor)
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        print("Saldo = ",self.saldo)

    def registrar_transacoes(self, tipo, valor):
        self.transacoes.append({"Tipo", tipo,"Valor", tipo})

#===============================================================#

class Conta_Corrente(ContaBancaria):
    def __init__(self, numero_conta, limite_cheque_especial = 0):
        super().__init__(numero_conta)
        self.limite_cheque_especial = limite_cheque_especial

    def emitir_cheque(self, valor):
        if self.saldo + self.limite_cheque_especial > valor:
            self.saldo -= valor
        else:
            print("Limite de cheque especial")
        
#===============================================================#

class Conta_Pupanca(ContaBancaria):
    def __init___(self, numero_conta, poupanca):
        super().__init__(self, numero_conta)
        self.poupanca = poupanca

