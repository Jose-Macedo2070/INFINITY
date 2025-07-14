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
'''
def add_tarefa():
    ...
# Funções: que eu preciso
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




tarefas = []

indice = 1


print(10* '-', 'MENU', 10* '-')
while True:

    opcao = int(input('Digite: \n[1]- Para adicionar uma nova tarfa; \n[0]- Para encerrar o código; \nDigite aqui: '))


    if opcao == 0:
        break

    elif opcao == 1:
        nome = input('Digite o nome da tarefa: ')
        descricao = input('Descreva a tarefa: ')
        categoria = input('Dê uma categoria tarefa: ')
        prioridade = int(input('Diga a prioridade da tarefa de 1 a 3, sendo 1 a mais baixa e 3 a mais alta : '))
    


        dicionario = {
        'ID': len(tarefas),
        'Nome': nome,
        'Descrição': descricao,
        'Categoria': categoria.lower(),
        'Prioridade': prioridade,
        'Concluido': False
        }
    
        tarefas.append(dicionario)
        print(tarefas)
        continue

        
'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''
# https://dontpad.com/projeto-funcoes

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

        print('-----')
        print(f'ID: {tarefas.index(tarefa)}')
        print(f'Nome: {tarefa['nome']}')
        print(f'Descrição: {tarefa['descricao']}')
        print(f'Categoria: {tarefa['categoria']}')
        print(f'Prioridade: {tarefa['prioridade']}')
        print(f'Status: {status}')

def exibir_tarefas_prioridade(prioridade):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma prioridade passada
    pass

def exibir_tarefas_categoria(categoria):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma categoria passada
    pass



desafio    
def remover_tarefas_categoria():


add_tarefa()
add_tarefa()
listar_tarefas()
print(tarefas)
'''






        
        

