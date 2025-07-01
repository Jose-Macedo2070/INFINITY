   # ATIVIDADE PRÁTICA 1

# Crie uma função chamada calcular_imc(peso, altura) que calcule e retorne o IMC de uma pessoa.

# Depois, crie outra função chamada classificar_imc(imc) que, com base no IMC calculado, retorne a categoria da pessoa.

# Por fim, crie um programa que peça ao usuário o peso e a altura, calcule o IMC e mostre o resultado com a classificação.


import funcoes_atv

# str_peso = input('Digite o peso do paciente: ')
# str_altura = input('Digite a altura do paciente: ')

# try:
#     peso_int = int(str_peso)
#     altura_float = float(str_altura)

# except ValueError:
#     print('Digite apenas números.')

# imc = funcoes_atv.calcular_imc(peso_int, altura_float)

# print(f'O imc do paciente é de {imc:.2f}.') 

# print(funcoes_atv.classificar_imc(imc))





# ATIVIDADE PRÁTICA 2

# Crie um programa que permita ao usuário cadastrar produtos.

# Cada produto deve ter:

# - Nome

# - Preço

# O programa deve permitir o cadastro de quantos produtos o usuário quiser, e ao final, exibir uma lista com todos os produtos cadastrados.

# OBS:

# - Cada produto deve ser armazenado como um dicionário dentro de uma lista.

# - Crie duas funções obrigatórias:

# a) cadastrar_produto – para adicionar um produto

# b) exibir_produtos – para mostrar todos os produtos

# Dúvidas:
'''
1- tem como fazer o import sem precisar criar uma lista no arquivo separado tambem?
2- porque meu for não deu certo na função exibir?
'''







import funcoes_atv
produtos = []


while True:

    opcao = int(input('Digite: \n[1] para cadastrar um produto; \n[2] para exibir a lista; \n[0] para encerrar. \nsua resposta aqui: '))

    # try:
    #     opcao_int = int(opcao)
    
    # except ValueError:
    #     print('Digite apenas números')



    if opcao == 0:
        print('Obrigado pelo cadastro, encerrando o programa')
        break


    elif opcao == 1:
        nome = input('Digite o nome do produto: ')
        valor = float(input('Digite quanto custa o produto: '))
        funcoes_atv.cadastrar_produto(nome, valor)
        print(f'Produto {nome} custando R${valor:.2f} foi cadastrado com sucesso! ')
        continue
    
    elif opcao == 2:
        print('Aqui está sua lista até agora:')
        print(funcoes_atv.exibir_produtos())
        continue
    
    
    
    else:
        print('Opção inválida, tente algo do menu.')
        continue
    

















# ATIVIDADE PRÁTICA 3

# Crie um programa que permita ao usuário converter temperaturas entre:

# 1) Celsius para Fahrenheit

# 2) Fahrenheit para Celsius

# 3) Celsius para Kelvin

# O programa deve exibir um menu de opções, o usuário escolhe a conversão e informa a temperatura.

# Funções obrigatórias:

# - celsius para fahrenheit

# - fahrenheit para celsius

# - celsius para kelvin

# (Opcional: criar uma função para exibir o menu e outra para validar escolha)



