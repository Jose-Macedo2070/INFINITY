
# função feita para contar letras sem os espaços
def contar_letras(string):
    
    string_sem_espaços = string.replace(" ", "")
    return (f'A(s) palavra(s) "{string}" tem {len(string_sem_espaços)} letra(s)')



# função feita para contar palvras em frases
def contar_palavras(string):
    contador_palavras = 0
    for i in string:
        if i == " ":
            contador_palavras +=1
    return (f'Tem {contador_palavras + 1} palavra(s) na frase "{string}"')




# função feita para inverte palavras ou frases
def inverter_str(string):
 
    return (f'A(s) palavra(s) "{string}" invertida(s) fica(m) assim: {string[::-1]}')




# função feita para verificar se a plavra é um palindromo
def verificar_palindromo(string):

    if string[::-1] == string:
        return (f'"{string} "É um palindromo')
    return (f'"{string}" Não é um palindromo')
    
