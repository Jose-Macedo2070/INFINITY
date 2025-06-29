''' 
# Métodos úteis pra tudo (listas, tuplas, sets, dicts)

# ---------LISTAS/TUPLAS---------

lista.append(...) # Adiciona um elemento ao final da lista
lista.insert(..., ...) # Adiciona um elemento na posição informada
lista.remove(...) # Remove um elemento de uma lista através de seu valor
lista.pop('índice') # Remove um elemento de uma lista através de seu índice
del (lista['indice']) # Deleta itens de uma lista pelo indice do elemento  
'elemento'['índice'] # Modifica e substitui o item do índice informado
lista.count( 'elemento' ) # mostra quantas vezes o elemento aparece em uma lista ou tupla
lista.index('elemento') #mostra o índice de um elemento de uma lista ou tupla
len(lista)	# mostra quantos elemento tem numa lista ou em uma tupla
sum(lista)	# soma os elementos numérics de uma lista ou tupla
max(lista)	# mostra o maior elemento numérico de uma lista ou tupla
min(lista)	# mostra o menor elemento numérico de uma lista ou tupla

# ---------SETS---------

sets.add(...) # Serve para adicionar novos itens.
sets.update('set2') # Serve para adicionar itens de outro conjunto ao set especificado.
sets.remove(...) # Remove o valor do set especificado mas se esse valor não existir dá erro e quebra o código.
sets.discard(...) # Remove  o valor do set especificado e não quebra o código caso o valor não exista.
sets.intersection('set2') # Retorna um novo conjunto contendo apenas os itens presentes em ambos.
sets.intersection_update('set2') # Atualiza o 1º conjunto o deixando apenas com o contendo presente em ambos os conjuntos iniciais.
sets.union('set2') # OU sets | set2	 Retorna a união dos dois conjuntos ultilizados.

# ---------dicts---------

for i in dict.items():	# Busca no dicionário a chave e seu valor correspondente
    ...
for i in dict.values():	# Busca apenas os valores de cada chave dentro do dicionário
    ...
for i in dict.keys():	# Busca apenas as chaves dentro do dicionário
    ...
dicts['string']	# Para acessar um valor de um dicionário basta printarmos o dicionário e colocar entre colchetes e aspas a chave que queremos.
dict.get('valor') # Também podemos utilizar a função get() para acessar um valor. No .get() podemos após o valor  comum passar um valor para ser printado no terminal caso ela não seja encontrada.
dict.fromkeys( 'iteravel' )	# Cria um novo dicionário com chaves proveniente do iteravel (uma lista, um dicionário), os valores por padrão serão None

del (dicts['chave']) # Deleta itens de um dicionario pela chave do valor  



# ---------LISTAS/TUPLAS---------
# indice:    0     1  2     3
lista = ['string', 8, 9.0, True] #sintaxe
    #       str,  int, float, bool

tuplas = ('string', 8, 9.0, True)

lista_vazia = [] #sintaxe para criar lista vazia
tupla_vazia = () #sintaxe para criar tupla vazia
# ... = Valor
# ..., ... = posição/indice, valor


# METODOS:
lista.append(...) # Adiciona um elemento ao final da lista
lista.insert(..., ...) # Adiciona um elemento na posição informada
lista.remove(...) # Remove um elemento de uma lista através de seu valor
lista.pop('índice') # Remove um elemento de uma lista através de seu índice
'elemento'['índice'] # Modifica e substitui o item do índice informado
lista.count( 'elemento' ) # mostra quantas vezes o elemento aparece em uma lista ou tupla
lista.index('elemento') #mostra o índice de um elemento de uma lista ou tupla
len(lista)	# mostra quantos elemento tem numa lista ou em uma tupla
sum(lista)	# soma os elementos numérics de uma lista ou tupla
max(lista)	# mostra o maior elemento numérico de uma lista ou tupla
min(lista)	# mostra o menor elemento numérico de uma lista ou tupla

#--------------------------------------------------------------------



# ---------SETS---------
# indice:    0     1  2     3
sets = {'string', 8, 9.0, True} #sintaxe
    #       str,  int, float, bool


sets_vazio = set() #sintaxe para criar lista vazia
# sets_vazio = {} #sintaxe errada essa confusão gera um dissionário

# ... = Valor
# ..., ... = posição/indice, valor


sets.add(...) # Serve para adicionar novos itens.
sets.update('set2') # Serve para adicionar itens de outro conjunto ao set especificado.
sets.remove(...) # Remove o valor do set especificado mas se esse valor não existir dá erro e quebra o código.
sets.discard(...) # Remove  o valor do set especificado e não quebra o código caso o valor não exista.
sets.intersection('set2') # Retorna um novo conjunto contendo apenas os itens presentes em ambos.
sets.intersection_update('set2') # Atualiza o 1º conjunto o deixando apenas com o contendo presente em ambos os conjuntos iniciais.
sets.union('set2') # OU sets | set2	 Retorna a união dos dois conjuntos ultilizados.



#--------------------------------------------------------------------


# ---------dicts---------
# indice:    0     1  2     3
dicts = {'string': 'opa', 
         'numero': 8, 
         'numero_float': 9.0,  #sintaxe
         'boleano': True
         } 


dict_vazia = {} #sintaxe para criar um dicionário vazio

# ... = Valor
# ..., ... = posição/indice, valor


for i in dict.items():	# Busca no dicionário a chave e seu valor correspondente
    ...
for i in dict.values():	# Busca apenas os valores de cada chave dentro do dicionário
    ...
for i in dict.keys():	# Busca apenas as chaves dentro do dicionário
    ...
dicts['string']	# Para acessar um valor de um dicionário basta printarmos o dicionário e colocar entre colchetes e aspas a chave que queremos.
dict.get('valor') # Também podemos utilizar a função get() para acessar um valor. No .get() podemos após o valor  comum passar um valor para ser printado no terminal caso ela não seja encontrada.
dict.fromkeys( 'iteravel' )	# Cria um novo dicionário com chaves proveniente do iteravel (uma lista, um dicionário), os valores por padrão serão None

'''