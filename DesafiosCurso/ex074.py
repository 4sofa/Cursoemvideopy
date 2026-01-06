from random import randint
menor = 0
maior = 0
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
while True:
    for d in range(0, len(tupla)):
        print(f'{tupla[d]}', end=' ')
        if d == 0:
            menor = tupla[d]
            maior = tupla[d]
        else:
            if tupla[d] < menor:
                menor = tupla[d]
            if tupla[d] > maior:
                maior = tupla[d]
    break
print(f'\nO maior número é {maior}')
print(f'O menor número é {menor}')
