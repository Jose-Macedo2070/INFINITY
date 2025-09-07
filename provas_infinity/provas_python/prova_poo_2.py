# [PYIA-A12]  Crie uma classe base chamada Veiculo que tenha um método chamado movimentar. Este método deve imprimir a mensagem "Veículo está em movimento." para indicar que qualquer veículo está em movimento. Em seguida, crie duas subclasses chamadas Carro e Moto que herdem de Veiculo. Dentro de cada uma dessas subclasses, sobrescreva o método movimentar para imprimir mensagens específicas para cada tipo de veículo. Na classe Carro, o método movimentar deve imprimir "Carro está dirigindo.", enquanto na classe Moto, o método deve imprimir "Moto está acelerando."

class Veiculo:

    def movimentar(self):
        return 'veiculo está em movimento'
    

class Moto(Veiculo):

    def movimentar(self):
        return 'Moto está acelerando'
    

class Carro(Veiculo):

    def movimentar(self):
        return 'Carro está dirigindo'
    

monza = Carro()
pop_100 = Moto()

print(monza.movimentar())
print(pop_100.movimentar())
        