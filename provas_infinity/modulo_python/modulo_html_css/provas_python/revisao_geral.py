# [PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.






produtos ={}

print('----CADASTRO DE PRODUTOS----')
while True:

    opcao = int(input('Digite [1] para adicionar um produto, digite pelo menos 5 itens ou [0] para encerrar o programa: '))


    if opcao == 0:
        print('Após a lista o programa será encerrado!')
        print('Aqui estam os produtos cadastrados:') 
        
        print(produtos)
        print(f'O total da sua compra foi {sum(produtos.values())}')

        break

    elif opcao == 1:
        nome = input('Digite o nome do produto: ')
        valor = float(input('Digite o valor do produto: '))
        produtos[nome] = valor
        continue