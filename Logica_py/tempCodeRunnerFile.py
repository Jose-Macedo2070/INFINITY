num1 = int(input('Digite o primeiro número do intervalo: '))
num2 = int(input('Digite o último número do intervalo: '))


while num1 <= num2:

    if num1 % 2 == 0:
        print (num1)
        num1 += 2