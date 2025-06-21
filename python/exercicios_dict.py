# # ex 12

# lula = 0
# bossonaro = 0
# pablo = 0

# candidatos = { 
#     'Lula': '',
#     'Bossonaro': '',
#     'Pablo Marçal': ''
# }

# print('Bem vindo(a) as  eleições de 2026!')
# print('Aqui está a lista de candidatos')
# print('-------------------------')

# for candidato in candidatos:
#     print(candidato)

# print('-------------------------')
# while True:


#     print('Veja a opção que melhor te atende:')

#     print(' Digite 1 para votar em Lula; \n Digite 2 para votar em Bossonaro; \n Digite 3 para votar em Pablo Marçal; \n Digite 0 para encerrar o programa.')
#     print('-------------------------')

#     opcao = int(input('Digite sua escolha: '))

#     if opcao == 0:
#         print('Obrigado por paticipar, seu voto foi contabilizado')
#         print('--------------------------------------------------')

#         print('Os dados finais do dict estão assim:')
#         candidatos['Lula'] = lula
#         candidatos['Bossonaro'] = bossonaro
#         candidatos['Pablo Marçal'] = pablo
#         print (candidatos)
#         # print(f' Lula tem {lula} votos; \n Bossonaro tem {bossonaro} votos; \n Pablo Marçal tem {pablo} votos.')
#         break

#     elif opcao == 1:
#         lula += 1
#         print('Você votou no Candidato Lula')
#         print('Voto contabilizado')
#         print('-------------------------')
#         continue

#     elif opcao == 2:
#         bossonaro += 1
#         print('Você votou no Candidato Bossonaro')
#         print('Voto contabilizado')
#         print('-------------------------')
#         continue

#     elif opcao == 3:
#         pablo += 1
#         print('Você votou no Candidato Pablo Marçal')
#         print('Voto contabilizado')
#         print('-------------------------')
#         continue
    
#     else:
#         print('Número inválido, verifique se digitou certo e tente novamente.')
#         print('-------------------------')


dicionario = {'Chave1': '', 'Chave2': '', 'Chave3': '', 'Chave4': ''}


del(dicionario['Chave1'])


lista_chaves = ['Chave1', 'Chave2', 'Chave3', 'Chave4']


todas_existem = True

for chave in lista_chaves:

    if chave not in dicionario:
        todas_existem = False
        break


print(todas_existem)








