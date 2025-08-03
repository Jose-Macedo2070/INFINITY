# ATIVIDADE PRÁTICA 2

# Crie um dicionário com informações de produtos,
# incluindo nome, preço e quantidade em estoque.
# Implemente funções para adicionar, remover e atualizar
# produtos no dicionário.



# produto = {
#     'Nome': 'pc',
#     'preco': 2000.00,
#     'estoque': 50
# }




lista_produtos = []


def add_produto():
    nome = input('digite o nome do produto: ').lower()
    preco = float(input('digite o valor do produto: '))
    estoque = int(input('digite quantos temos no estoque: '))

    produto = {
        'nome': nome,
        'preco': preco,
        'estoque': estoque
    }

    lista_produtos.append(produto)
    return ( f"Produto {produto['nome']}, cadastrado com sucesso")

def listar_produtos():
        # Percorrer a lista de lista_produtos
    if len(lista_produtos) == 0:
        return 'Lista de lista_produtos vazia'

    for produto in lista_produtos:
        # status = 'Concluído' if tarefa['concluido'] else 'Pendente'

        print(f"ID: {lista_produtos.index(produto)}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']}")
        print(f"Estoque: {produto['estoque']}")
        print(10 * '-')





print(add_produto())
listar_produtos()


def remove_produto():
    excluir_id = int(input('Digite o "ID" o produtoque você quer excluir: '))
    lista_produtos.pop(excluir_id)
    return f'A tarefa com o ID: {excluir_id} foi excluida com sucesso. '

def update_produto():
    ...



# while True:
#     opcao = input('Digite: \n[1]-Cadastrar um produto \n[2]-Remover um produto \n[3]-Atualizar um produto \n[0]-Encerrar o programa')

#     if opcao == 0:
#         break

#     elif opcao == 1:
#         ...

#     elif opcao == 2:
#         ...

#     elif opcao == 3:
#         ...