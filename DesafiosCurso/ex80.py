lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista')
    else:
        for posicao, valor in enumerate(lista):
            if n <= valor:
                lista.insert(posicao, n)
                print(f'Valor inserido na posição {posicao}')
                break

print(lista)
