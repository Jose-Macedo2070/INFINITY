from func_calculadora import *
from func_manipu_str import *

'''
Dúvidas para próxima aula:
1- dá pra fazer o import de uma função lambda?





'''


# ATIVIDADE PRÁTICA 1

# Crie um programa que será uma calculadora.

# Nesta calculadora você deverá ter um módulo para as
# operações matemáticas, o arquivo principal deverá
# conter apenas um menu de escolha para o usuário

# (soma, subtração, multiplicação e divisão).


num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

print(f'seus números somados {somar(num1,num2)}')
print(f'seus números subtraidos {subitrair(num1,num2)}')
print(f'seus números multiplicados {multiplicar(num1,num2)}')
print(f'seus números divididos {dividir(num1,num2)}')




# ATIVIDADE PRÁTICA 2

# Crie um módulo chamado manipulacao_strings que
# contenha funções para realizar operações com strings,
# como inverter uma string, contar o número de palavras
# em uma string e verificar se uma string é um
# palíndromo (lê-se igual de trás para frente). Crie
# um programa principal que importe o módulo e use
# essas funções com strings fornecidas pelo usuário.


# fazer um menu com  opcao
