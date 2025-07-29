# ATIVIDADE PRÁTICA 1
# Dada uma lista de números, crie uma nova lista contendo
# apenas os números pares.


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]



numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
numeros_impares = list(filter(lambda x: x % 2 == 1, lista_numeros))


print(numeros_impares)
print(numeros_pares)