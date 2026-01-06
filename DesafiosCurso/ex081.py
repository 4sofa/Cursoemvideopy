lista = []
a = 0
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if resp in 'N':
        break

for posicao, valor in enumerate(lista):
    if valor == 5:
        a += 1
print('-='*40)
print(f'Foram digitados {len(lista)} numeros na lista')
lista.sort(reverse=True)
print(f'\nA lista de valores em ordem decrescente \n{lista}')

if 5 in lista:
    print('O valor 5 está na lista')
    print(f'Encontrei o valor 5, {a} vezes na lista')
else:
    print('O valor 5 não está na lista')
print('')
print('-='*40)
