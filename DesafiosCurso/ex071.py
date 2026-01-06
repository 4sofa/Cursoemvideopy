print('-'*40)
print(' '*11, 'CAIXA ELETRONICO')
print('-'*40)

valor = int(input('Digite o valor a ser sacado: R$'))
ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1
a = b = c = d = 0
while True:
    print('-'*40)
    print('[ 1 ] para cedulas de R$50')
    print('[ 2 ] para cedulas de R$20')
    print('[ 3 ] para cedulas de R$10')
    print('[ 4 ] para cedulas de R$1')
    opcao = int(input('Escolha uma opção: '))
    while opcao < 1 or opcao > 4:
        print('ERRO! Digite novamente')
        opcao = int(input('Escolha uma opção: '))
    quant = int(input('Digite o numero de cedulas: '))
    print('-'*40)
    while quant == 0:
        print('ERRO! Digite novamente')
        quant = int(input('Digite o numero de cedulas: '))

    if opcao == 1:
        if valor < ced50*quant:
            print('Você nao pode retirar este valor, tente novamente')
        if valor >= ced50*quant:
            valor -= 50*quant
            a += 1*quant
            print(f'Você sacou {ced50*quant} reais!, restam {valor} reais')

    if opcao == 2:
        if valor <= ced20*quant:
            print('Voce nao pode retirar este valor, tente novamente')
        if valor >= ced20*quant:
            valor -= 20*quant
            b += 1*quant
            print(f'Voce sacou {ced20*quant} reais!, restam {valor} reais')

    if opcao == 3:
        if valor < ced10*quant:
            print('Voce nao pode retirar este valor, tente novamente')
        if valor >= ced10*quant:
            valor -= 10*quant
            c += 1*quant
            print(f'Voce sacou {ced10*quant} reais, restam {valor} reais!')

    if opcao == 4:
        if valor < ced1*quant:
            print('Voce nao pode retirar este valor, tente novamente')
        if valor >= ced1*quant:
            valor -= 1*quant
            d += 1*quant
            if valor == 1:
                print(f'Voce sacou {ced1*quant} real, restam {valor} reais!')
            else:
                print(f'Voce sacou {ced1*quant} reais, restam {valor} reais!')

    if valor == 0:
        break
print('-'*40)
print(f'Voce sacou {a} cedulas de R$50')
print(f'Voce sacou {b} cedulas de R$20')
print(f'Voce sacou {c} cedulas de R$10')
print(f'Voce sacou {d} cedulas de R$1')
