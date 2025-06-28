# Métodos úteis pra tudo (listas, tuplas, sets, dicts)


# ---------LISTAS---------
# indice:    0     1  2     3
lista = ['string', 8, 9.0, True] #sintaxe
    #       str,  int, float, bool


lista_vazia = [] #sintaxe para criar lista vazia

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

