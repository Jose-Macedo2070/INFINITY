# POO 2:

# '''A herança serve para fascilitar o trabalho de digitação muito basicamente,
# temos uma class base e normalmente não ultilizaremos ela e sim as que herdaram ela'''

# class Pessoa:
#     def __init__(self, nome, endereco, email):
#         self.nome = nome
#         self.enderco = endereco
#         self.email = email

#     def dados_pessoais(self):
#         return f'nome: {self.nome}\nemail: {self.email}' # as funções criadas são chamadas junto com o super tambem


# #para a chamada da herança criamos uma class comum e colocamos a base dentro dos parenteses para chamarmos ela
# # Sintaxe : class NomeEspecifico(Nome da classe que vai herdar)


# class PessoaFisica(Pessoa):
#     def __init__(self, nome, endereco, email, cpf):
#         super().__init__(nome, endereco, email) # o super é criado automaticamente e serve para fascilitar o trabalho e ele faz os selfs. pra gente, após ele eu posso colocar o especifico dessa classe em si
#         self.cpf = cpf


#     def dados_pessoais(self): #o idela é passar o mesmo nome da função feita na base e se quisermos podemos colocar o dado extra que queremos que apareça
#         return f'{super().dados_pessoais()}\nCpf: {self.cpf} ' #aqui colocamos o dado extra que queremos que apareça



# class PessoaJuridica(Pessoa):
#     def __init__(self, nome, endereco, email, cnpj):
#         super().__init__(nome, endereco, email) 
#         self.cnpj = cnpj


#     def dados_pessoais(self): #o idela é passar o mesmo nome da função feita na base e se quisermos podemos colocar o dado extra que queremos que apareça
#         return f'{super().dados_pessoais()}\nCnpj:{self.cnpj} ' #aqui colocamos o dado extra que queremos que apareça
    



# pf1 = PessoaFisica('jose', 'qualquer rua', 'jose@gmail.com', 11111111111)
# print(pf1.dados_pessoais())



# atv_1:

# class Formas:
#     def __init__(self, base, altura, diametro, raio):
#         self.base = base
#         self.altura = altura
#         self.diametro = diametro
#         self.raio = raio



# class Retangulo(Formas):
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def calcular_area(self):
#         return self.base * self.altura 
    





# retangulo = Retangulo(8, 9)

# print(retangulo.calcular_area())


# atv_2

# class Veiculo:
#     def __init__(self, modelo, cor ):
#         self.cor = cor
#         self.modelo = modelo

#     def tipo(self):
#         return f'O(A) {self.modelo} tem a cor {self.cor}'
    


# class Bicicleta(Veiculo):
#     def __init__(self, cor, modelo):
#         super().__init__(cor, modelo)

#     def tipo(self):
#         return f'{super().tipo()} e é uma bicicleta' 

# class Carro(Veiculo):
#     def __init__(self, cor, modelo):
#         super().__init__(cor, modelo)

#     def tipo(self):
#         return f'{super().tipo()} e é um carro'
    

# carro_1 = Carro('celta', 'prata')
# bike_1 = Bicicleta('caloi', 'preta')


# print(carro_1.tipo())
# print(bike_1.tipo())


# atv_3

# class Calculadora:
#     def __init__(self, a, b):
#       self.a = a
#       self.b = b


#     def somar(self):
#       return f'{self.a + self.b}'
    

# class String(Calculadora):
#     def __init__(self, a, b):
#       super().__init__(a, b)

#     def somar(self):
#        return super().somar()
    

# class Inteiros(Calculadora):
#     def __init__(self, a, b):
#       super().__init__(a, b)

#     def somar(self):
#        return super().somar()
   

# concatenar_str = String('ao', 'ba')
# somar_inteiros = Inteiros(5, 5)



# print(concatenar_str.somar())
# print(somar_inteiros.somar())

   


# atv_4
# class Veiculo:
#     def __init__(self):
#         pass

#     def acelerar(self):
#         return f'{__class__.__name__} acelera até'
    
#     def frear(self):
#         return f'tem freio à'


    


# class Bicicleta(Veiculo):
#     def __init__(self):
#         super().__init__()

#     def acelerar(self):
#         return f'A {__class__.__name__} {super().acelerar()} no maximo uns 40km'

# # class Carro(Veiculo):




# bike_1 = Bicicleta()

# print(bike_1.acelerar())



# atv_5

#(base)
# class Animal:
#     def emitirSom(self):
#         pass

# class Cachorro(Animal):
#     def emitirSom(self):
#         return "au au"


# class Gato(Animal):
#     def emitirSom(self):
#         return "miau"

# class Passaro(Animal):
#     def emitirSom(self):
#         return "piu"

# def fazerAnimalFalar(animal):
#     return animal.emitirSom()


# ruby = Cachorro()
# mia = Gato()
# pipoca = Passaro()


# animais = [ruby, mia, pipoca ] 


# for animal in animais:
#     print(animal.__class__.__name__, 'faz', fazerAnimalFalar(animal))
