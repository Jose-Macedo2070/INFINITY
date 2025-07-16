
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
    return (f'Tarefa adicionada com sucesso')




def exibir_tarefas_prioridade(prioridade):
    # Percorrer a lista de tarefas e filtrar (if) as tarefas com a mesma prioridade passada
    for tarefa in tarefas:
        if tarefa['prioridade'] == 'alta':
            prioridade_alta.append(tarefa)
    return


while True:

    menu_1 = int(input('Digite: \n[1]- Nova tarefa; \n[2]- ; \n[0]- Encerrar o código; \nEscolha: '))


    if menu_1 == 0:
        print('Encerrando o código')
        break

    elif menu_1 == 1:
        print(add_tarefa())
        continue

    elif menu_1 == 2:
        # print('Aqui estão todas as tarefas listadas até agora: \n', 10 * '-' )
        exibir_tarefas_prioridade('alta')
        print(prioridade_alta)