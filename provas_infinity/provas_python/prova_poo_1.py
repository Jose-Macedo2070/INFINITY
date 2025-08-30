'''[PYIA-A11] Crie três classes separadas e independentes: Animal, Cachorro e Gato.
Cada classe deve ter um método chamado falar (), que imprime uma mensagem específica na tela:

- A classe Animal deve imprimir: "Este animal faz um som genérico."

- A classe Cachorro deve imprimir: "O cachorro está latindo."

- A classe Gato deve imprimir: "O gato está miando."

Regras:

- As classes não devem se relacionar entre si.

- Cada classe deve ser criada de forma independente.

- No final, crie um objeto para cada uma das classes e chame o método falar () de cada objeto.'''



class Animal:
    def __init__(self, animal):
        self.animal = animal

    def falar(self):
        return f'Este(a) {self.animal} faz um som genérico'
    
class Cachorro:
    def __init__(self, cachorro):
        self.cachorro = cachorro

    def falar(self):
        return f'O cachorro está latindo.'
    
class Gato:
    def __init__(self, gato):
        self.gato = gato

    def falar(self):
        return f'O gato está miando.'
    


raposa = Animal('raposa')
cachorro1 = Cachorro('cachorro1')
gato1 = Gato('gato1')


print(raposa.falar())
print(cachorro1.falar())
print(gato1.falar())
