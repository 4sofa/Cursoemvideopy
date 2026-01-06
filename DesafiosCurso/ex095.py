informacao = list()
gols = list()
d = 0
pessoas = 0
n = 0
infos = dict()

while True:
    infos = {'nome': str(input('Nome do jogador: ')).title().strip(),
             'partidas': int(input('Partidas jogadas: '))}
    if infos['partidas'] > 0:
        for c in range(infos['partidas']):
            gols.append(int(input(f'Quantos gols na partida {c}? ')))
            infos['gols'] = gols
            d += gols[c]
            infos['total'] = d
            n = infos['partidas']

    informacao.append(infos.copy())
    pessoas += 1
    print('-'*30)
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        print('-='*30)
        break

print('cod ', end='')
for i in infos.keys():
    print(f'{i:<15}', end='')
print()
print('-'*80)

for k, v in enumerate(informacao):
    print(f'{k:>3} ', end='')
    for valores in v.values():
        print(f'{str(valores):<15}', end='')
    print()
print('-'*80)

