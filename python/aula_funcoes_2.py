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

# numeros = [1, 2, 3, 4 ]
# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(numeros_pares)



'''ex 6: Crie uma função que aceita uma lista de strings e use a
função reduce (importada de functools) para encontrar
a maior string na lista.'''







'''ex 7: Crie uma função chamada criar_lista_de_compras que
aceita um número variável de itens de compras como
argumentos posicionais (usando *args). A função deve
criar e retornar uma lista de compras que contenha
todos os itens fornecidos.'''

# def criar_lista_de_compras(*args):
#     lista_de_compras.append(args)
#     return (f'o produto {args} foi adicionado com sucesso')


# def mostrar_lista_de_compras(lista):
#     print('atualmente esses são os produtos cadastrados')
#     for i in lista:
#         return (f'{i}')

# lista_de_compras = []

# while True:
#     opcao = int(input('Digite [1]- para cadastrar um item, \n[2]- para mostrar sua lista até agora ou \n[0] para encerrar o programa: '))


#     if opcao == 0:
#         print('Encerrando o código.')
#         break


#     elif opcao == 1:
#         produto = input('Digite o nome do produto: ')
#         print(criar_lista_de_compras(produto))
#         print(40 * '-')
#         continue
        


#     elif opcao == 2:
#         print(mostrar_lista_de_compras(lista_de_compras))


# como fazer passando um item de lista de cada vez






'''ex 8: Crie uma função que aceite dois números e uma
operação (por exemplo, adição, subtração,
multiplicação, divisão) como argumentos e use funções
lambda para realizar a operação especificada. A função
deve retornar o resultado da operação.'''

print('-' * 4, 'BEM VINDO A CALCULADORA', '-' * 4)


while True:
    num_1 = input('Digite um número inteiro: ')
    num_2 = input('Digite outro número inteiro: ')

    try:
        num_1_int = int(num_1)
        num_2_int = int(num_2)
        print('Escolha o quer fazer com os números.')
        opcao = int(input('Digite:\n[1] para somar; \n[2] para subtrair; \n[3] para multiplicar; \n[4] para dividir ou \n[0] para sair. '))
        
        if opcao == 0:
            print('Obrigado por ultilizar a nossa calculadora')
            break

        elif opcao == 1:
            soma = lambda x, y : x + y
            print(f'Soma: {soma(num_1_int, num_2_int)}')
            continue

        elif opcao == 2:
            subitracao = lambda x, y : x - y
            print(f'Subtração: {subitracao(num_1_int, num_2_int )}')
            continue

        elif opcao == 3:
            multiplicacao = lambda x, y : x * y
            print(f'Multiplicação: {multiplicacao(num_1_int, num_2_int)}')
            continue

        elif opcao == 4:
            divisao = lambda x, y : x / y
            print(f'Divisão: {divisao(num_1_int, num_2_int)}')
            continue
        
        else:
            print('Opção inválida, tente novamente')
        
    except:
        print('digite apenas números.')
        continue





