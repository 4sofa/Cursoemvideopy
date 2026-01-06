while True:
    n = int(input('Quer ver a tabuada de qual valor? [ -1 para parar ]: '))
    print('-'*30)
    if n > -1:
        for c in range(0, 10 + 1):
            print(f'{n} * {c} = {n * c}')
        print('-'*30)
    else:
        break

print('fim do programa')
