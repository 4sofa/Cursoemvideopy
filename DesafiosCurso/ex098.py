
from operator import neg


def contagem(inicio, fim, passo):
    print('Contagem de 1 até 10 de 1 em 1')
    a = 0
    while a != 10:
        print(f'{a}', end=' ')
        a += 1
        
    print(f'{a}', end=' ')
    print('FIM')
    print('Contagem de 10 até 0 de 2 em 2')
    a = 10


    while a != 0:
        print(f'{a}', end=' ')
        a -= 2

    print(f'{a}', end=' ')    
    print('FIM')

    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    while inicio <= fim:
        print(f'{inicio}', end=' ')
        inicio += passo
    
    while fim <= inicio:
        print(f'{inicio}', end=' ')
        inicio -= passo

    print(end=' ')
    print('FIM')
    


contagem(float(input('Inicio: ')), float(input('Fim: ')), float(input('Passo: ')))
