
'''Você possui dados de vendas trimestrais de uma
empresa em uma lista. Cada trimestre é representado
como uma lista de números, onde cada número
representa o valor de vendas de um mês (janeiro a
março, abril a junho, julho a setembro e outubro a
dezembro).
Você deve realizar as seguintes tarefas:
Calcule a média de vendas por trimestre.
Encontre o trimestre com a maior soma de vendas.
Encontre o trimestre com a menor soma de vendas.

Calcule o total de vendas no ano inteiro.

- Construa seus dados fictícios'''







primeiro_semestre = []
lista_anual = [

    [10, 20, 30],#(Jan, Fev, Mar)
    [40, 50, 60],#(Abr, Mai, Jun)
    [70, 80, 90],#(Jul, Ago, Set)
    [100, 110, 120]#(Out, Nov, Dez)

]

def media_semestre(lista):
    contador = 1
    for c in lista:
        media = sum(c) / len(c)
        print(f' a media do trimetre {contador}: foi: {media}')
        contador +=1

vendas_anuais = []

vendas_anuais.append(sum(lista_anual[0]))
vendas_anuais.append(sum(lista_anual[1]))
vendas_anuais.append(sum(lista_anual[2]))
vendas_anuais.append(sum(lista_anual[3]))

print(max(vendas_anuais))
print(min(vendas_anuais))
print(vendas_anuais)



# media_semestre(lista_anual)

# print(lista_anual[0])
# print(sum(lista_anual[0]))

# print(lista_anual[1])
# print(sum(lista_anual[1]))

# print(lista_anual[2])
# print(sum(lista_anual[2]))

# print(lista_anual[3])
# print(sum(lista_anual[3]))