lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if resp in 'N':
        break

for pos, c in enumerate(lista):
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)

print(f'Lista completa {lista}')
print(f'Lista de numeros pares {listapar}')
print(f'Lista de numeros impares {listaimpar}')
