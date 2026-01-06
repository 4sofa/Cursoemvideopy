a = float(input('Digite o número da primeira variavel: '))
b = float(input('Digite o segundo número da primeira variavel: '))
c = float(input('Digite o primeiro número da segunda variavel: '))


def regradetres(xx, yy, zz):
    x = (yy * zz) / xx
    return x


resultado = regradetres(a, b, c)
print('O valor de x é {}'.format(resultado))
