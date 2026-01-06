objeto = {}
dados = list()
for c in range(0, 2):
    objeto = {'Filme': str(input('Filme: ')),
              'Ano': int(input('Ano: ')),
              'Diretor': str(input('Diretor: '))}
    dados.append(objeto.copy())
for keys, values in objeto.items():
    print(f'O {keys} é {values}')
print('----------------------------------')
print(f'Os valores são:\n{objeto.values()}')
print(f'As chaves são :\n{objeto.keys()}')
print(f'Os itens são :\n{objeto.items()}')
print('----------------------------------')

for obj in dados:
    for keys, values in obj.items():
        print(f'O {keys} é {values}')
print('----------------------------------')
print(dados[0]['Filme'])
print(dados[1]['Filme'])
