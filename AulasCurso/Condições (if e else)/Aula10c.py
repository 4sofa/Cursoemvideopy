n1 = float(input('Digite sua primeiro nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 6:
    print('Você está acima da média com {:.1f}. Parabens!'.format(media))
else:
    print('Sua média foi {:.1f}, você ficou abaixo da media.'.format(media))
