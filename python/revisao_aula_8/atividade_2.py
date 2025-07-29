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
    return (f'Produto "{produto['nome']}", cadastrado com sucesso')



def lista
print(add_produto())
print(lista_produtos)






def remove_produto():
    ...

def update_produto():
    ...




