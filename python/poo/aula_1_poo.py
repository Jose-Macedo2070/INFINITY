#Molde = classe

# class Produto:

#     def __init__(self, nome, preco, quantidade=0): # método construtor
#         self.nome = nome
#         self.preco = preco
#         self.qtd  = quantidade

#     def vender(self, qtd_vendida=1):
#         if qtd_vendida > self.qtd:
#             return 'Quantidade insuficiente'

#         else:
#             self.qtd -= qtd_vendida


#     def abastecer(self, qtd_add):
#         self.qtd = qtd_add


#     def __str__(self): # serve para destrinchar os códigos de objeto

#         return f'{self.nome}, {self.preco}, {self.qtd}'


# #Objeto
# produto1 = Produto('Computador', 1500, 50)
# print(produto1.nome)  # o nome da variável seguido de ponto e o atributo que 
# print(produto1.preco) # queremos para acessarmos o dado que queremos
# print('vendendo produto (-5)')
# produto1.vender(5)
# print(10 * '-')

# print('quantidade atual:', produto1.qtd)
# print(10 * '-')

# print('adicionando estoque (+6)')
# produto1.abastecer(6)
# print(10 * '-')

# print('quantidade atual:', produto1.qtd)



# atv_1:
# class Cachorro:
#     def __init__(self, nome, raca, idade):
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade

#     def __str__(self):
#       return f'{self.nome}, {self.raca}, {self.idade}'
    



# cachorro_1 = Cachorro('ruby', 'maltês', 1)

# print(cachorro_1)




# atv_2:
# class Pessoa:
#     def __init__(self, nome, idade, peso, genero):
#         self.nome = nome 
#         self.idade = idade
#         self.peso = peso
#         self.genero = genero

#     def __str__(self):
#         return f'Meu nome é {self.nome}, tenho {self.idade} anos, peso {self.peso}kg e sou {self.genero}, é um prazer em conhece-lo(a)'
    


# pessoa1 = Pessoa('José', 24, 140, 'Homem') 

# print(pessoa1)



# atv_3:
# class Funcionarios:
#     def __init__(self, nome, cargo, salario):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = salario

#     def __str__(self):
#         return f'Nome: {self.nome} \nCargo: {self.cargo} \nSalário: R$ {self.salario:.2f}'
    

# class Empresa:
#     def __init__(self):
#         self.lista_funcionarios = []

#     def add_funciorarios(self, funcionario):
#         self.lista_funcionarios.append(funcionario)

#     def dell_funcionarios(self, funcionario):
#         self.lista_funcionarios.remove(funcionario)

#     def listar_funcionarios(self):
#         for i in self.lista_funcionarios:
#             print(f'Nome: {i.nome} \nCargo: {i.cargo} \nSalário: R$ {i.salario:.2f}')
#             print('-' * 30)

    
    
# # Criando objétos
# empresa1 = Empresa()
# funcionario1 = Funcionarios('José', 'dev', 6000)
# funcionario2 = Funcionarios('Aline', 'tech lead', 15000)

# # usando a função de adicionar pessoas
# empresa1.add_funciorarios(funcionario1)
# empresa1.add_funciorarios(funcionario2)

# # Listando 
# print('lista depois da adição dos funcionários')
# print('-' * 30)
# empresa1.listar_funcionarios()


# #  Excluindo pessoas 
# empresa1.dell_funcionarios(funcionario1)

# # Listando 
# print('lista depois de excluir o funcionário 1')
# print('-' * 30)

# empresa1.listar_funcionarios()




# atv_4
# class Calculadora:
#     def __init__(self, numero_1, numero_2, operacao):
#         self.numero_1 = numero_1
#         self.numero_2 = numero_2
#         self.operacao = operacao

   
#     def __str__(self):

#         if self.operacao == '+':
#             return f'{self.numero_1} + {self.numero_2} = {self.numero_1 + self.numero_2}'
        
#         elif self.operacao == '-':
#             return f'{self.numero_1} - {self.numero_2} = {self.numero_1 - self.numero_2}'
        
#         elif self.operacao == '*':
#             return f'{self.numero_1} + {self.numero_2} = {self.numero_1 * self.numero_2}'
        
#         elif self.operacao == '/':
#             return f'{self.numero_1} + {self.numero_2} = {self.numero_1 / self.numero_2:.2f}'
    




# # Digite os dois numeros e a operação desejada entre ("+", "-", "*", "/")
# calculo_1 = Calculadora(5, 7, '+')
# calculo_2 = Calculadora(5, 7, '-')
# calculo_3 = Calculadora(5, 7, '*')
# calculo_4 = Calculadora(5, 7, '/')

# print(calculo_1)
# print(calculo_2)
# print(calculo_3)
# print(calculo_4)




# atv_5

# Crie uma classe chamada Fatura , a classe Fatura deve incluir os seguintes atributos o nome do item; o preço unitário do item; quantidade de item a ser faturado; valor total da fatura; Sua classe deve ter um construtor que inicialize todos os atributos menos o valor total da fatura. Forneça um método chamado gerar_fatura que calcula o valor da fatura (isto é, multiplicar a quantidade pelo preço por item).


# class Fatura:
#     def __init__(self, nome_item, preco_item, qtd_item):
#         self.nome_item = nome_item
#         self.preco_item = preco_item
#         self.qtd_item = qtd_item
#         self.valor_total = 0


#     def gerar_fatura(self):
#         self.valor_total = self.preco_item * self.qtd_item
#         print(f'Fatura atual: R$ {self.valor_total:.2f}')



#     def __str__(self):
#         return f'Nome: {self.nome_item}\nValor Unitário: R$ {self.preco_item:.2f}\nEm Estoque: {self.qtd_item}'
    



# item1 = Fatura('Computador', 3000, 7)


# print(item1)
# item1.gerar_fatura()



# DESAFIO PRÁTICO
'''Crie uma classe Hotel que permita gerenciar
funcionários, reservas e quartos de hotel. Os
funcionários devem ter informações como nome,
função e salário. O hotel deve ser capaz de
receber reservas, atribuí-las a quartos e
calcular a conta final.

CRIAR CLASSES:
- HOTEL (LISTAS DAS CLASSES P/ GERENCIAR)
- FUNCIONARIOS (NOME, CARGO, SALÁRIO)
- RESERVAS
- QUARTOS

QUE METODOS FAZER:
- ADICIONAR OBJETOS( FUNCIONARIOS, RESERVA, QUARTOS)
- LISTAR COM FOR
- FAZER A CONTA DE (TEMPO RESERVADO * VALOR DA DIÁRIA)


HOTEL: DEVE CONSEGUIR RECEBER A RESERVA E DEPOIS ALOCAR A UM QUARTO CALCULANDO A DIÁRIA


'''








class Hotel:
    def __init__(self):
        self.lista_funcionarios = []
        # self.lista_quartos = []
        self.lista_reservas = []

    def add_funcionarios(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def fazer_reserva(self, reserva):
        self.lista_reservas.append(reserva)
        
    def listar_funcionario(self):
        for i in self.lista_funcionarios:
            print(f'Nome: {i.nome_funcionario} \nCargo: {i.funcao} \nSalário: R$ {i.salario:.2f}')
            print('-' * 30)

    def chekout(self):
        for i in self.lista_reservas:
            print(f'A reserva do {i.numero_do_quarto} ficou no valor de R$ {i.valor_da_diaria * i.tempo_alugado}.00')
        

class Funcionario:
    def __init__(self, nome_funcionario, funcao, salario ):
        self.nome_funcionario = nome_funcionario
        self.funcao = funcao
        self.salario = salario


    def __str__(self):
        return f'Nome: {self.nome_funcionario}\nFunção: {self.funcao}\nSalário {self.salario}'




class Reservas:
    def __init__(self, numero_do_quarto, valor_da_diaria, tempo_alugado):
        self.numero_do_quarto = numero_do_quarto
        self.valor_da_diaria = valor_da_diaria
        self.tempo_alugado = tempo_alugado

    def __str__(self):
        return f'Número do Quarto: {self.numero_do_quarto}\nValor da Diária: R${self.valor_da_diaria:.2f}\nTempo Alugado: {self.tempo_alugado} dias'



#objétos
hotel = Hotel()
funcionario1 = Funcionario('José', 'Recepção', 5000)
funcionario2 = Funcionario('aline', 'gerente', 8000)
reserva1 = Reservas('Quarto 1', 50, 25)

# adicionando
hotel.add_funcionarios(funcionario1)
hotel.add_funcionarios(funcionario2)
hotel.fazer_reserva(reserva1)


# listando
hotel.listar_funcionario()
hotel.chekout()