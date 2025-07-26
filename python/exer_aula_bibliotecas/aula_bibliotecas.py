from func_exerc_bibliotecas import *



# ATIVIDADE PRÁTICA 3

# Crie um programa que permite ao usuário calcular a
# área e o perímetro de formas geométricas simples,
# como quadrados, retângulos e círculos. Use funções
# matemáticas do módulo math para realizar os cálculos.

while True:
    opcao = int(input('Digite: \n[1]- Para calcular área \n[2]para calcular o perimétro \n[0]- ecerrar o código \nopção: '))
    

    if opcao == 0:
        break

    elif opcao == 1:
        area = int(input('Digite a forma que quer calcular a área: \n[1]-Quadrado \n[2]-retângulo \n[3]-circulo'))

        if area == 1:
            print(calcular_area_quadrado())
        
        elif area == 2:
            print(calcular_area_retangulo())
    





# ATIVIDADE PRÁTICA 4

# Desenvolva um jogo de adivinhação em que o programa
# escolhe um número aleatório e desafia o jogador a
# adivinhá-lo. Forneça dicas ao jogador, indicando se o
# número é maior ou menor do que a adivinhação atual.






# ATIVIDADE PRÁTICA 5

# Desenvolva um programa que permita ao usuário
# converter entre diferentes unidades de medida, como
# metros para pés, quilogramas para libras, ou Celsius
# para Fahrenheit. Use módulos que contenham funções

# de conversão.