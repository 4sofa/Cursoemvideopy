from random import randint
quant = 0
while True:
    print('-='*20)
    print('[1] PAR')
    print('[2] IMPAR')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        computador = randint(0, 10)
        jogador = int(input('Digite um valor: '))
        print('-=' * 20)
        print(f'O computador escolheu {computador} e você escolheu {jogador}')
        s = computador + jogador
        if s % 2 == 0:
            print(f'O total deu {s} foi par')
            print('Voce venceu!')
            quant += 1
            print('Vamos jogar novamente...')
        else:
            print(f'O total deu {s} foi impar')
            print('Voce perdeu!')
            break
    if opcao == 2:
        computador = randint(0, 10)
        jogador = int(input('Digite um valor: '))
        s = computador + jogador
        print(f'O computador escolheu {computador} e você escolheu {jogador}')
        if s % 2 == 1:
            print('O total deu {s} foi impar')
            print('Voce venceu!')
            print('Vamos jogar novamente...')
            quant += 1
        else:
            print(f'O total deu {s} foi par')
            print('Voce perdeu!')
            break
    if opcao != 1 and opcao != 2:
        print('Opção Invalida. Tente Novamente!')

if quant == 0:
    print('Você nao venceu nenhuma vez')
else:
    print(f'Você venceu {quant} vezes')
print('GAME OVER!')
