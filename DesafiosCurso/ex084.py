lista = list()
dados = list()
while True:
    lista.append(str(input('Digite seu nome: ')).capitalize().strip())
    lista.append(int(input('Digite seu peso: ')))
    dados.append(lista[:])
    lista.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar not in 'SN':
        continuar = str(input('ERROR! Digite novamente! [S/N]: '))
    elif continuar in 'N':
        break

pessoapesada = list()
pessoaleve = list()
for nome, peso in dados:
    if peso <= 70:
        pessoaleve.append(nome)
    elif peso >= 100:
        pessoapesada.append(nome)
print('-='*40)
print(f'Lista das pessoas mais pesadas: ', end='')
for c in pessoapesada:
    print(f'[{c}]', end=' ')
print()
print('-='*40)
print('Lista das pessoas mais leves: ', end='')
for c in pessoaleve:
    print(f'[{c}]', end=' ')
print()
print('-='*40)
print(f'Número de pessoas cadastradas: {len(dados)}')