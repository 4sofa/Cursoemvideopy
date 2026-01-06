from random import randint
from time import sleep
from operator import itemgetter

print('Valores sorteados:')
dados = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
for k, v in dados.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(1)

print('Ranking de posições')
a = 0
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for k, v in ranking:
    a += 1
    print(f'    {a}° Lugar {k} com o valor {v}')
    sleep(1)
    # ou
# for i, v in enumerate(ranking):
#   print(f'{i} lugar: {v[0]} com {v[1]}.')
# i = indice - numeração
# v = valor. Ex: v[0] = o nome dos jogadores e v[1] = valor do dado