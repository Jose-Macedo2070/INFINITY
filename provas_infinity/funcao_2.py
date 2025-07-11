# [PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.

def maior_numero(*args):
    return max(args)

print(maior_numero(5, 2, 3))



