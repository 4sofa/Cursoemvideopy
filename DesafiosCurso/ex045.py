from time import sleep
from random import randrange

# Crie um programa que faça o computador jogar jokenpo com voce
# pedra, papel ou tesoura
print('\033[31m-=-\033[m'*20)
print(' '*25, '\033[33mJokenpô\033[m')
print('\033[31m-=-\033[m'*20)
print('\033[36mEscolha pedra, papel ou tesoura.\033[m')
print('\033[37m[ 1 ] Pedra\033[m')
print('\033[35m[ 2 ] Tesoura\033[m')
print('\033[33m[ 3 ] Papel\033[m')
usuario = int(input('Escolha uma das opções: '))
computador = randrange(1, 3)
print('PROCESSANDO...')
sleep(1)
print('PROCESSANDO..')
sleep(0.90)
print('PROCESSANDO.')
sleep(0.80)
if computador == 1 and usuario == 2:
    print('Você escolheu Tesoura, o computador escolheu Pedra')
    print('\033[31mVocê Perdeu\033[m')
elif computador == 2 and usuario == 3:
    print('Você escolheu Papel, o computador escolheu Tesoura')
    print('\033[31mVocê Perdeu\033[m')
elif computador == 3 and usuario == 1:
    print('Você escolheu Pedra, o computador escolheu Papel')
    print('\033[31mVocê Perdeu\033[m')
elif computador == 1 and usuario == 3:
    print('Você escolheu Papel, o computador escolheu Pedra')
    print('\033[32mVocê Venceu, Parabens!\033[m')
elif computador == 3 and usuario == 2:
    print('Você escolheu Tesoura, o computador escolheu Papel')
    print('\033[32mVocê Venceu, Parabens!\033[m')
elif computador == 2 and usuario == 1:
    print('Você escolheu Pedra, o computador escolheu Tesoura')
    print('\033[32mVocê Venceu, Parabens!\033[m')
elif computador and usuario == 1 or computador and usuario == 2 or computador and usuario == 3:
    print('Empate!')
else:
    print('\033[31mOpção Invalida. Tente Novamente!\033[m')
