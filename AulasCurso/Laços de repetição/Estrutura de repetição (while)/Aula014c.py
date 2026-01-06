n = 1
npar = 0
nimpar = 0
print('DIGITE [0] PARA ENCERRAR')
while n != 0:
    n = int(input('Digite um inteiro: '))
    '''if n == 0:
        break'''
    if n != 0:
        if n % 2 == 0:
            npar += 1
        if n % 2 == 1:
            nimpar += 1

print(f'Pares: {npar} Impares: {nimpar}')
