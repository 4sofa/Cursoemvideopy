infos = {'nome': str(input('Nome do jogador: ')).title().strip(),
         'partidas': int(input('Partidas jogadas: '))}

a = infos['partidas']
lista = list()
d = 0
if a != 0:
    for c in range(a):
        lista.append(int(input(f'Quantos gols na partida {c+1}? ')))
        d += lista[c]

infos['total'] = d
infos['gols'] = lista
print('-='*20)
print(infos)
print('-='*20)
print(f'O campo nome tem o valor {infos["nome"]}')
print(f'O campo gols tem o valor {lista}')
print(f'O campo total tem o valor {infos["total"]}')
print('-='*20)
print(f'O jogador {infos["nome"]} jogou {infos["partidas"]} partidas')
if a != 0:
    for c in range(a):
        print(f'    => Na partida {c+1}, fez {lista[c]} gols.')

print(f'Foi um total de {infos["total"]} gols')
