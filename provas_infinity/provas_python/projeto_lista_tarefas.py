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
prioridade_alta = []
prioridade_media = []
prioridade_baixa = []


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


def marcar_como_concluido():
    # Pegar a tarefa (nome, índice, etc) e marcar o status como concluído
    id = int(input('Digite o ID da tarefa que deve ser concluída: '))
    tarefas[id]['concluido'] = True #testar depois como fazer uma lista separada para separar as concluidas das pendentes
    

def listar_tarefas():
    # Percorrer a lista de tarefas
    if len(tarefas) == 0:
        return 'Lista de tarefas vazia'

    for tarefa in tarefas:
        status = 'Concluído' if tarefa['concluido'] else 'Pendente'

        print(f'ID: {tarefas.index(tarefa)}')
        print(f'Nome: {tarefa["nome"]}')
        print(f'Descrição: {tarefa["descricao"]}')
        print(f'Categoria: {tarefa["categoria"]}')
        print(f'Prioridade: {tarefa["prioridade"]}')
        print(f'Status: {status}')
        print(10 * '-')

def exibir_tarefas_prioridade(prioridade):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma prioridade passada
    for tarefa in tarefas:
        if tarefa['prioridade'] == 'alta':
            prioridade_alta.append(tarefa)

        if tarefa['prioridade'] == 'media':
            prioridade_media.append(tarefa)
    
        if tarefa['prioridade'] == 'baixa':
            prioridade_baixa.append(tarefa)
    return



def exibir_tarefas_categoria(categorias):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma categoria passada
    encontrou = False  

    for tarefa in tarefas:
        if tarefa['categoria'] == categorias.lower():
            status = 'Concluído' if tarefa['concluido'] else 'Pendente'

            print(f'Aqui estão as tarefas com categoria {categoria}:')
            print(f'ID: {tarefas.index(tarefa)}')
            print(f'Nome: {tarefa["nome"]}')
            print(f'Descrição: {tarefa["descricao"]}')
            print(f'Categoria: {tarefa["categoria"]}')
            print(f'Prioridade: {tarefa["prioridade"]}')
            print(f'Status: {status}')
            print(10 * '-')

            encontrou = True

    if not encontrou:
        print('Nenhuma tarefa com essa categoria foi encontrada.')


def remover_tarefas():
    # lista.pop('índice') # Remove um elemento de uma lista através de seu índice
        id = int(input('Digite o ID da tarefa que deve ser removida: '))
        tarefas.pop(id)
        return f'A tarefa com o ID: {id} foi excluida com sucesso. '



while True:

    menu_1 = int(input('Digite: \n[1]- Nova tarefa; \n[2]- Listar tarefas; \n[0]- Encerrar o código; \nEscolha: '))


    if menu_1 == 0:
        print('Encerrando o código')
        break

    elif menu_1 == 1:
        add_tarefa()
        print('Tarefa adicionada com sucesso')
        print(40 * '-')
        continue

    elif menu_1 == 2:
        print('Aqui estão todas as tarefas listadas até agora: \n', 10 * '-' )
        listar_tarefas()
        
        menu_2 = int(input('Digite: \n[1]- Exibir tarefas por prioridade; \n[2]- Exibir tarefas por categoria; \n[3]- Remover tarefas; \n[4]- Concluir tarefa; \n[0]- Voltar para o menu anterior; \nEscolha: '))
        
        if menu_2 == 0:
            continue

        elif menu_2 == 1:
            exibir_tarefas_prioridade('prioridades')

            print('Aqui estão as tarefas de prioridade alta:\n', 10 * '-')

            for tarefa in prioridade_alta:
                status = 'Concluído' if tarefa['concluido'] else 'Pendente'

                print(f'Nome: {tarefa["nome"]}')
                print(f'Descrição: {tarefa["descricao"]}')
                print(f'Categoria: {tarefa["categoria"]}')
                print(f'Prioridade: {tarefa["prioridade"]}')
                print(f'Status: {status}')
                print(10 * '-')



            print('Aqui estão as tarefas de prioridade media:')

            for tarefa in prioridade_media:
                status = 'Concluído' if tarefa['concluido'] else 'Pendente'

                print(f'Nome: {tarefa["nome"]}')
                print(f'Descrição: {tarefa["descricao"]}')
                print(f'Categoria: {tarefa["categoria"]}')
                print(f'Prioridade: {tarefa["prioridade"]}')
                print(f'Status: {status}')
                print(10 * '-')



            print('Aqui estão as tarefas de prioridade baixa:')
            
            for tarefa in prioridade_baixa:
                status = 'Concluído' if tarefa['concluido'] else 'Pendente'

                print(f'Nome: {tarefa["nome"]}')
                print(f'Descrição: {tarefa["descricao"]}')
                print(f'Categoria: {tarefa["categoria"]}')
                print(f'Prioridade: {tarefa["prioridade"]}')
                print(f'Status: {status}')
                print(10 * '-')

        elif menu_2 == 2:
            categoria = input('Digite a categoria que deseja ver: ').lower()
            exibir_tarefas_categoria(categoria)



        elif menu_2 == 3:
            # remover tarefa
            print(remover_tarefas())
            print('Suas tarefas agora são essas:')
            listar_tarefas()

        elif menu_2 == 4:
            # concluir tarefa
            print(marcar_como_concluido())


