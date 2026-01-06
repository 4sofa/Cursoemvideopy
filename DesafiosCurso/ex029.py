velocidade = float(input('Digite a velocidade de um carro em Km/h: '))
if velocidade <= 80:
    print('Você não foi multado.')
elif velocidade > +80:
    multa = 7.00 * (velocidade - 80)
    print('Você foi multado em {:.2f} reais'.format(multa))
