# Crie um programa que leia dois valores e mostre um menu na tela
sair = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
while sair != 5:
    print(' ' * 20)
    print('MENU DE OPCOES')
    print('1 - SOMAR')
    print('2 - MULTIPLICAR')
    print('3 - MAIOR')
    print('4 - NOVOS NUMEROS')
    print('5 - SAIR')
    opçao = int(input('ESCOLHA UMA OPCAO: '))
    print(' ' * 20)
    if opçao == 1:
        print(f'{n1} + {n2} = {n1 + n2}!')
    if opçao == 2:
        print(f'{n1} * {n2} = {n1 * n2}!')
    if opçao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    if opçao == 4:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite um numero: '))
    if opçao == 5:
        sair = 5

print('FIM DO PROGRAMA')
