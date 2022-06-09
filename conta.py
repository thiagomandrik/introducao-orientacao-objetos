class Conta():
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo de {} na conta de {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        print("Deposito realizado na conta de {} no valor de {}".format(self.__titular, valor))

    def __tem_saldo_disponivel_para(self, valor_a_verificar):
        valor_disponivel_a_retirar = self.__saldo + self.__limite
        return valor_a_verificar <= valor_disponivel_a_retirar

    def sacar(self, valor):
        if self.__tem_saldo_disponivel_para(valor):
            self.__saldo -= valor
            print("Saque relizado na conta de {} no valor de {}".format(self.__titular, valor))
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if self.__tem_saldo_disponivel_para(valor):
            self.sacar(valor)
            conta_destino.depositar(valor)
        else:
            print("Saldo insuficiente.")
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}


# conta1 = Conta(123, "Thiago", 1700, 2000.00)
# conta1.extrato()
# conta1.depositar(50)
# conta1.extrato()
# conta1.sacar(500.55)
# conta1.extrato()

# conta2 = Conta(223, "Luiza", 50000.00, 150000.00)
# conta2.extrato()