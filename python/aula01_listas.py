# lista_numeros = [ 1, 2, 3, 4, 5 ]

# print(lista_numeros)

# listas_vogais = [ 'a', 'e', 'i', 'o', 'u' ]

# print(listas_vogais)

# usuário = ['José', 24, True]

# print(usuário[2])


# Lista com as cinco primeiras vogais do alfabeto

# letras = [ 'a', 'b', 'c', 'd' , 'e' ]
# print(letras[-1]) # letra 'e'
# print(letras[-2]) # letra 'd'
# print(letras[-3]) # letra 'c'
# print(letras[-4]) # letra 'b'
# print(letras[-5]) # letra 'a'



# # Adicionando intens ao final da lista com método .append()
# numero = [ 1, 2, 3, 4, 5 ]
# numero.append(6)

# print(numero) # terminal = [ 1, 2, 3, 4, 5, 6 ]

# # Adicionando itens em dada posição da lista com método .insert()

# numero = [ 10, 30, 40, 50 ]
# letras = [ 'a', 'e', 'o', 'u' ]
# pesos = [ 1.2, 3.4, 5.3, 6.7 ]

# # Inserindo valores nas respectivas posições das listas
# numero.insert(1, 20) #inserindo 20 na posição 1
# letras.insert(2, 'i') #inserindo i na posição 2
# pesos.insert(2, 4.0) #inserindo 4.0 na posição 2

# # Exibindo as inserções dos valores
# print(numero) #terminal = [ 10, 20, 30, 40, 50 ]
# print(letras) #terminal = [ 'a', 'e', 'i', 'o', 'u' ]
# print(pesos) #terminal = [ 1.2, 3.4, 4.0, 5.3, 6.7 ]


# # Removendo itens pelo indice com .pop()
# notas = [
# 9.0, # indice 0
# 8.7, # indice 1
# 9.9, # indice 2
# 8.7, # indice 3
# 7.9  # indice 4
# ]
# notas.pop(0) #removendo a nota 9.0
# notas.pop(1) #removendo a nota 9.9
# notas.pop(2) #removendo a nota 7.9


# print(notas) #terminal = [8.7, 8.7]

# Lista com nomes dos alunos finalistas

# finalistas = [
# 'josé',
# 'juliana',
# 'silvania',
# 'silvia',
# 'ronaldo'
# ]

# # Utilizando o método .remove() para remover um finalista
# finalistas.remove('silvania')

# # Exibindo a lista após a remoção do finalista
# print(finalistas) #terminal = ['josé', 'juliana', 'silvia', 'ronaldo']

# print(finalistas.index('josé')) # ultilizado para saber qual o índice do elemnto em questão

# palestrante_1 = ('Fernando Gomes', 'Agentes de ia no mercado de trabalho', 'Unifatecie')
# palestrante_2 = ('Juliana de Freitas', 'Influência da midia no tribunal do jure', 'Uninassau')
# palestrante_3 = ('José Macêdo', 'Segredos do Front-end', 'Dev em dobro')

# print(palestrante_3)
# print(f'Nome do Palestrante: {palestrante_3[0]};\n Tema da Palestra: {palestrante_3[1]};\n Instituição: {palestrante_3[2]}.') 








""" Suponha que você está gerenciando uma competição esportiva e tem
uma lista de tuplas representando os resultados das equipes em
diferentes modalidades. Cada tupla contém o nome da equipe, seguido
por uma lista de pontuações obtidas em cada rodada da competição.
 """
#exemplo   
# lista = [
#     ('sport', [2, 6]),
#     ('santa', [3, 7]),
#     ('nautico', [4, 8]),
#     ('retro', [5, 9]),
# ]

# medias = []
# classificacao = []
# for i, j in lista:
#     media = sum(j) / len(j)
#     medias.append((i, media))
#     classificacao.append((i, media))

# print(classificacao)

# print(f'  Tabela de classificação: \n ----------------------------------- \n 1º lugar:{classificacao[3]}\n 2º lugar:{classificacao[2]}\n 3º lugar:{classificacao[1]} \n 4º lugar:{classificacao[0]} ')



#1.Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista chamada medias.
#3.Crie uma nova lista chamada classificacao que contém tuplas, onde cada tupla contém o nome da equipe e sua média de pontuações.
#4.Exiba na tela a classificação final das equipes, mostrando o nome da equipe e sua média, da equipe com a pontuação mais alta para a mais baixa.










