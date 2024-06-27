# calculo ano bissexto
ano = int(input('Digite um ano para verificar se ele é bissexto: '))
if ano % 400 == 0 and ano % 4 == 0:
    print('Ele é')
else:
    print('nao é')
