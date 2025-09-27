'''
[PYIA-A13] Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. Crie um método depositar que permita adicionar um valor ao saldo, um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), e um método exibir_saldo que exiba o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque.'''




class ContaBancaria:
    def __init__(self, titular, saldo ):
        self.__titular = titular
        self.__saldo = saldo


    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular


    def set_saque(self, retirada):
        if retirada > self.__saldo:
            return "Seu saldo é insuficiente"
    
        elif retirada <= self.__saldo:
            self.__saldo -= retirada
            return f"Saque realizado com sucesso, seu saldo atual é de {self.__saldo}"
        
    def set_depositar(self, entrada):
        self.__saldo += entrada
        return f"Depósito realizado com sucesso, seu saldo atual é de {self.__saldo}"





conta_jose = ContaBancaria("josé", 5000)

# saldo = conta_jose.get_saldo()
print(conta_jose.get_saldo())
print(conta_jose.get_titular())
print(conta_jose.set_saque(1000))
print(conta_jose.set_depositar(70))
print(conta_jose.get_saldo())
