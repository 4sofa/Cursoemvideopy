# Verifique todas as possibilidades sempre
n1 = int(input('Escreva um numero: '))
if n1 > 1:
    print('{} é maior que 1'.format(n1))
elif n1 == 1:
    print('seu número é igual {}'.format(n1))
elif n1 == 0:
    print('Seu número é igual a {}'.format(n1))
else:
    print('Seu número é menor que 1')
