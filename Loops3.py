def q1():
    num = 0
    while(num <=10):
        print(num)
        num += 1

def q2():
    num = 10
    while(num >= 0):
        print(num)
        num -= 1

def q3():
    num = 0
    while(num <= 10):
        if num%2 == 0:
            print(num)
        num += 1

def q4():
    numero = int(input('Digite um número: '))
    num = 0
    while(num <=10):
        print(numero+num)
        num += 1

def q5():
    while(True):
        nome = str(input('Digite um nome: '))
        if nome == 'parar':
            break

def q6():
    while(True):
        num = int(input('Digite qualquer número, ou digite "0" para sair: '))
        if num > 0:
            num1 = int(input('Digite um número: '))
            print (f'{num+num1}')
        elif num == 0:
            break

    
q6()
