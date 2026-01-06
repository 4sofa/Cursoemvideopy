from random import randint
from time import sleep
palpites = 1
print('=-' * 20)
print(' '*15, 'J x B')
print('=-' * 20)
computador = randint(0, 10)
print('Digite [-1] para encerrar o programa.')
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
while jogador != computador and jogador != -1:
    while 0 <= jogador > 10:
        print('Número invalido. Tente Novamente!')
        jogador = int(input('Em que número eu pensei? '))
        print('PROCESSANDO...')
        sleep(1)
    else:
        if jogador != computador:
            print('Você errou. Tente Novamente!')
            if jogador < computador:
                print('O numero que eu pensei foi maior!')
                sleep(1)
            else:
                print('O numero que eu pensei foi menor!')
                sleep(1)
            jogador = int(input('Em que número eu pensei? '))
            print('PROCESSANDO...')
            sleep(1)
            palpites += 1

print('FIM DE JOGO!')
if jogador == computador:
    print(f'Parabéns, eu pensei no número {computador}!')
    print(f'Você precisou de {palpites} tentativas para acertar!')
