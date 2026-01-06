from random import randrange
from time import sleep
print('-=-' * 10)
print('vou pensar em um numero entre 0 e 5...')
print('-=-' * 10)
sleep(5)     # este sleep serve para dar uma cooldown, tempo de espera entre as respotas do computador
computador = randrange(0, 5)     # faz o computador sortear um numero entre 0 e 5
usuario = int(input('Em que número eu pensei? '))   # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
print('O usuario venceu!'if usuario == computador else 'O computador venceu, o número foi {}!'.format(computador))
