'''
- ID
- Nome 
- Descrição
- Categoria
- Prioridade
- status

Métodos:
- listar tarefas (for)
- marcar a tarefa concluída
  - nome
  - id
  - índice
- exibir a tarefa prioridade/categoria
  - for
  - qual a prioridade/categoria (if)
-adicionar tarefa
  - criar o dicionário
  - adicionar na lista

- Menu interativo (while)
'''



''' -------------------- como é pra ser:
tarefas = [{
    'ID': 0,
    'Nome': 'limpar quarto',
    'Descrição': 'organizar tudo',
    'Categoria': 'casa',
    'Prioridade': 2,
    'status': True
}]

# Funções: que eu preciso


def add_tarefa():
    ...
def marcar_como_concluido():
    # Pegar a tarefa (nome, índice, etc) e marcar o status como concluído
    ...

def listar_tarefas():
    # Percorrer a lista de tarefas
    ...

def exibir_tarefas_prioridade(prioridade):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma prioridade passada
    ...

def exibir_tarefas_categoria(categoria):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma categoria passada
    ...
'''



tarefas = []

def add_tarefa():
    nome = input('Digite a nome da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    categoria = input('Digite a categoria: ')
    prioridade = input('Digite a prioridade: ')

    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'categoria': categoria.lower(),
        'prioridade': prioridade.lower(),
        'concluido': False
    }

    tarefas.append(tarefa)
    return (f'Tarefa adicionada com sucesso')

def marcar_como_concluido():
    # Pegar a tarefa (nome, índice, etc) e marcar o status como concluído
    id = int(input('Digite o ID da tarefa que deve ser concluída: '))
    tarefas[id]['concluido'] = True

def listar_tarefas():
    # Percorrer a lista de tarefas
    if len(tarefas) == 0:
        return 'Lista de tarefas vazia'

    for tarefa in tarefas:
        status = 'Concluído' if tarefa['concluido'] else 'Pendente'

        print(f'ID: {tarefas.index(tarefa)}')
        print(f'Nome: {tarefa['nome']}')
        print(f'Descrição: {tarefa['descricao']}')
        print(f'Categoria: {tarefa['categoria']}')
        print(f'Prioridade: {tarefa['prioridade']}')
        print(f'Status: {status}')
        print(10 * '-')

def exibir_tarefas_prioridade(prioridade):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma prioridade passada
    pass

def exibir_tarefas_categoria(categoria):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma categoria passada
    pass


def remover_tarefas_categoria():
    ...



while True:

    menu_1 = int(input('Digite: \n[1]- Nova tarefa; \n[2]- Listar tarefas; \n[0]- Encerrar o código; \nEscolha: '))


    if menu_1 == 0:
        print('Encerrando o código')
        break

    elif menu_1 == 1:
        print(add_tarefa())
        continue

    elif menu_1 == 2:
        print('Aqui estão todas as tarefas listadas até agora: \n', 10 * '-' )
        print(listar_tarefas())
        
        menu_2 = input('Digite: \n[1]- Exibir tarefas por prioridade; \n[2]- Exibir tarfas por categoria; \n[0]- Voltar para o menu anterior; \nEscolha: ')
        
        if menu_2 == 0:
            continue












print(tarefas)
