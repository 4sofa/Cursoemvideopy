lista = []
resposta = 'S'
a = None
while True:
    a = int(input('Digite um valor: '))

    while a in lista:
        print('Valor duplicado! Não vou adicionar...')
        break

    while a not in lista:
        print('Valor adicionado')
        lista.append(a)
        break

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'S':
        continue
    if resposta in 'N':
        break

lista.sort()
print('-='*30)
print('Você digitou os seguintes valores em ordem crescente:'
      f'{lista}')
