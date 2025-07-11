# def funcao(*args) | sintaxe argumento posicional *args
#  print(args)      | sem o '*' para chamar
#                   | gera uma tupla

# def funcao(**kargs) | sintaxe argumento posicional **kargs
#  print(kargs)       | sem os '**' para chamar
#                     | gera um dicionário

# variavel = lambda parametro: comando  |  sintaxe função lambda
# soma = lambda x, y: x + y


# variavavel = list(map(função, lista)) | sintaxe metodo map()
# lista = [1,2,3]
# dobro = list(map(lambda x: x* 2, lista)) | map() tem que está envolto em uma lista 
# print(dobro)                             | para não retornar um objeto, ideal sempre 
#                                          | com função lambda depois o iteravel





# variavavel = list(filter(função, lista)) | sintaxe metodo map()
# lista = [1,2,3]
# dobro = list(filter(lambda x: x* 2, lista)) | filter() tem que está envolto em uma 
# print(dobro)                                | lista para não retornar um objeto, 
#                                             | ideal sempre com função lambda depois  
#                                             | o iteravel


# falta reduce





# ativiadades:

'''
ex 1: Crie um programa que solicita ao usuário que insira três notas e, em seguida, 
calcule a média dessas notas usando uma função. 
A função deve receber as três notas como argumentos e retornar a média. 
Por fim, o programa deve imprimir a média calculada.
'''
# def media(*args):
#     print(args)
#     return sum(args) / len(args)

# numeros = []

# while True:

#     opcao = int(input('1 pra adicionar e 0 para encerrar: '))


#     if opcao == 0:
#         print(media(*numeros)) # '*' serve para desempacotar a lista dentro da tupla 
#         break                  #  que o args gera.
                               

#     elif opcao == 1:
#         notas = float(input('digite números: '))
#         numeros.append(notas)
#         continue

'''ex 2: Crie um programa que define uma função
calcular_area_retangulo que recebe dois argumentos,
comprimento e largura de um retângulo, e retorna a
área desse retângulo. Em seguida, o programa deve
solicitar ao usuário que insira o comprimento e a
largura e imprimir a área calculada.'''

# função simples
# def area_retangulo(b, h):
#     return b * h
    
# base = float(input('Digite a base do retangulo: '))
# altura = float(input('Digite a altura do retangulo: '))
# print(area_retangulo(base, altura))


# resolução com lambda
# calculo = lambda b, h : b * h
# print(calculo(base, altura))


'''ex 3: Crie uma função chamada concatenar_strings que
aceita um número variável de strings como argumentos
posicionais (usando *args). A função deve concatenar
todas as strings em uma única string e retorná-la.'''


# def concatenar_strings(*args):

#     print(args)

#     resultado = ''
#     for i in args:
#         resultado += i 
    
#     return resultado

# print(concatenar_strings('oi', ' zé'))


'''ex 04: Crie uma função que aceita uma lista de números e use
a função map para retornar uma nova lista contendo o dobro de cada número na lista de entrada.'''

# def dobrar_lista(numero): 
#     for i in numeros:
#         i *= 2
#         dobro.append(i)

#     return dobro

# numeros = [1, 2, 3, 4, 5]
# dobro = []
# print(numeros)
# print(dobrar_lista(numeros))


# função lambda
# dobro = list(map(lambda x: x * 2, numeros ))
# print(dobro)

'''ex 05: Crie uma função que aceita uma lista de números e use
a função filter para retornar uma nova lista contendo apenas os números pares da lista de entrada.'''

numeros = [1, 2, 3, 4 ]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)











'''ex 7: Crie uma função chamada criar_lista_de_compras que
aceita um número variável de itens de compras como
argumentos posicionais (usando *args). A função deve
criar e retornar uma lista de compras que contenha
todos os itens fornecidos.'''