# Desafio:

# Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair.
# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)

# Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.

# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse
# exercício.

#  fazer isso com while true, seleção,  input fora da função e fazer uma função pra cada operação 


import funcoes_operacoes

print('-' * 4, 'BEM VINDO A CALCULADORA', '-' * 4)

while True:

    global_num1 = input('Digite um número inteiro: ') 
    global_num2 = input('Digite outro número inteiro: ') 

    try:
        
        int_global_num1 = int(global_num1)
        int_global_num2 = int(global_num2)


        print('Escolha o quer fazer com os números.', '\n', 40* '-')
        opcao = int(input('Digite:\n[1] para somar; \n[2] para subtrair; \n[3] para multiplicar; \n[4] para dividir ou \n[0] para sair. \nsua opção é: '))
        
        if opcao == 0:
            print('Obrigado por ultilizar a nossa calculadora')
            break

        elif opcao == 1:
            print(funcoes_operacoes.soma(global_num1, global_num2))
            print(40 *'-')
            continue

        elif opcao == 2:
            print(funcoes_operacoes.subtracao(global_num1, global_num2))
            print(40 *'-')
            continue

        elif opcao == 3:
            print(funcoes_operacoes.multiplicacao(global_num1, global_num2))
            print(40 *'-')
            continue

        elif opcao == 4:
            print(funcoes_operacoes.divisao(global_num1, global_num2))
            print(40 *'-')
            continue
        
        else:
            print('Opção inválida, tente novamente')
        
    except ValueError:
        print('digite apenas números inteiros.')
        continue





































