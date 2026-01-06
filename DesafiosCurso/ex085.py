def ex085():
    numeros = list()
    impar = list()
    par = list()
    lista = list()
    for c in range(7):
        lista.append(int(input(f'Digite o {c+1}° número: ')))
        if lista[c] % 2 == 0:
            par.append(lista[c])
        if lista[c] % 2 != 0:
            impar.append(lista[c])

    numeros.append(impar[:])
    numeros.append(par[:])
    del lista
    del par
    del impar
    numeros[0].sort()
    numeros[1].sort()
    print(f'Números pares: {numeros[1]}')
    print(f'Números impares: {numeros[0]}')


ex085()
