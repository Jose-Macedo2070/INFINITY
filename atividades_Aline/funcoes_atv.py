''' ---------------Função para calcular o imc '''
def calcular_imc(peso, altura):
    return  peso / (altura ** 2)



''' ---------------Função para classificar o imc '''
def classificar_imc(imc):

    if imc > 10 and imc <= 18.5:
        return ('o paciente está abaixo do seu peso ideal')
    
    elif imc > 18.5 and imc <= 24.9:
        return ('o paciente está com um peso adequado: ')
    
    elif imc >= 25 and  imc >= 29.9: 
        return ('o paciente está acima do peso')
    




''' ---------------Função para cadastrar um produto '''
produtos = []
def cadastrar_produto(produto, custo):

    return produtos.append({produto: custo})


''' ---------------Função para exibir uma lista de produtos '''
def exibir_produtos():
    
    return produtos