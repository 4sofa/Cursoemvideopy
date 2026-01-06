produtos = ('Geladeira', 500.00,
            'Leite', 9.99,
            'Lápis', 1.75,
            'Borracha', 1.50,
            'Computador', 5000.00)
print('-'*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('-'*40)
for posicao in range(len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='R$ ')
    else:
        print(f'{produtos[posicao]:>7.2f}')

print('-'*40)
print(f"{'FIM DO PROGRAMA':^40}")
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<34} ', end='')
    print(f'R$ {produtos[c+1]:>7.2f}')
print('-'*45)
