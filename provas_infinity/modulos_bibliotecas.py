# [PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.

from random import randint

def lancar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f'O número do primeiro dado é  "{dado1}" e o número do segundo  dado é o "{dado2}"')  #| caso queira ver os números
   
    return dado1 + dado2
    




print(lancar_dados())  

