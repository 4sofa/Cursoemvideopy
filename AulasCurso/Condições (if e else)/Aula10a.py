calculo = float(input('Escreva um numero para fazer uma multiplicação: '))
calculo2 = float(input('Escreva outro número: '))
resultado = calculo * calculo2

if resultado < 0:
    print('Seu resultado da um número negativo\n{}'.format(resultado))
else:
    print('Seu resultado da um número positivo\n{}'.format(resultado))
print(15*'-', 'Fim', 15*'-')
