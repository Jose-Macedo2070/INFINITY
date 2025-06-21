#  1 Conversão de Unidades:
# Crie um programa que converta metros para centímetros.
# Peça ao usuário para digitar um valor em metros, armazene
# em uma variável e converta para centímetros.num = float(input('Digite um número em metros: '))

# centimetros = num / 100

# print(f'O numeor em metros é {num} e em centimétros é {centimetros} .')  


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#  2 Cálculo de Área:
# Crie um programa que calcule a área de um retângulo.
# Peça ao usuário para digitar a largura e a altura,
# armazene em variáveis e calcule a área. 


#   base = int(input('Digite um número para a base do retândgulo: '))
# altura = int(input('Digite um número para a altura do retângulo: '))

# print(f' {base} x {altura} = {base * altura}') 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#   3 Cálculo de IMC:
# Crie um programa que calcule o Índice de Massa Corporal (IMC).
# Peça ao usuário para digitar seu peso e altura, armazene em
# variáveis e calcule o IMC. 

# peso = int(input('Digite o peso do paciente: '))
# altura = float(input('Digite a altura do paciente: '))

# imc = peso / (altura ** 2)

# print(f'O imc do paciente é de {imc:.2f}.') 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#  4 Cálculo de Juros Simples:
# Crie um programa que calcule o valor futuro de um investimento
# usando a fórmula de juros simples. Peça ao usuário para digitar o
# capital inicial, a taxa de juros e o tempo de aplicação. 

#  J = C × i × t 

#  c = float(input('Digite seu capital: '))
# juros = float(input('Digite sua taxa de juros: '))
# t = int(input('Digite o tempo de aplicação: '))
# i = juros / 100

# j = c * i * t 
# print(f' Sua aplicação vai ser de {j}. ') 



# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#  5 Verificando a Média do Aluno:
# Crie um algoritmo que peça quatro notas de um aluno, calcule a
# média e exiba se o aluno foi aprovado ou reprovado (média >= 6). 

# nota1 = float(input('Digite sua nota aqui: '))
# nota2 = float(input('Digite sua nota aqui: '))
# nota3= float(input('Digite sua nota aqui: '))
# nota4 = float(input('Digite sua nota aqui: '))

# media = (nota1 * nota2 * nota3 * nota4) / 4

# print(media) 


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#  6 Algoritmo de Cálculo de Desconto:
# Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual
# de desconto. 

# produto = float(input('Qual o valor do produto em R$: '))
# desconto = float(input('de quando foi o desconto: '))
# desconto_aplicado = (produto - ((desconto / 100) * produto))

# print(f'O valor original do produto é R$ {produto:.2f}, o desconto foi de {desconto}%, logo o cliente pagará R$ {desconto_aplicado:.2f} .')





# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#  7 Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos. 

 
# eu fiz:
# segundos = float(input('Quantos segundos se passaram: '))
# minutos = segundos / 60
# horas = minutos / 60

# print(f' se passaram {horas:.0f} horas/ {minutos:.0f} minutos/ {segundos:.2f} segundos.') 

# professora: 



# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 8 Categoria de Idade:
# Desenvolva um programa que peça a idade do usuário e
# informe se ele é criança, adolescente, adulto ou idoso.


# idade = int(input('Digite sua idade aqui: '))

# if 0 < idade < 12:
#     print('É criança.')

# elif 12 <= idade < 18:
#     print('É adolescente.')

# elif 18 <= idade < 62:
#     print('É adulto.')

# else:
#     print('É idoso.')


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Classificação de Notas:
# Crie um programa que solicite uma nota de 0 a 100
# e informe o conceito (A, B, C, D, F) com base na nota.

nota = float(input('Digite uma nota de 0 a 100 para saber qual a sua categoria: '))





if 100 <= nota > 79 :
    print('Categoria A')

elif  79 > nota > 59 :
    print('Categoria B')

elif  58 > nota > 39:
    print('Categoria C')

elif  38 > nota > 19 :
    print('Categoria D')

elif  19 > nota > 10 : 
    print('Categoria E')

else:
    print('Categoria F')

