from os import listdir


# [PYIA-A08] Importe o módulo 'os' e use a função 'listdir' para listar todos os arquivos e pastas presentes no diretório onde o script Python está sendo executado. A função 'listdir' retornará uma lista contendo os nomes dos arquivos e pastas. Após obter essa lista, exiba cada item da lista individualmente na saída do console.

def listar_arquivos():
    lista_de_pastas = listdir()
    for indice, valor in enumerate(lista_de_pastas):
        print(f'A pasta {indice} se chama {valor}')



listar_arquivos()