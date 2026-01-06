lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))

print(f'Os valores da lista foram {lista}')

print(f'O menor valor foi {min(lista)} nas posições', end=' ')
for pos, c in enumerate(lista):
    if c == min(lista):
        print(f'{pos}... ', end='')

print(f'\nO maior valor foi {max(lista)} nas posições', end=' ')
for pos, c in enumerate(lista):
    if c == max(lista):
        print(f'{pos}... ', end='')
