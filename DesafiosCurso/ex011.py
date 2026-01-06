lar = float(input('Coloque em metros a largura da sua parede: '))
alt = float(input('Coloque em metros a altura da sua parede: '))
area = lar * alt
tinta = area / 2
print('A sua parede tem uma dimensão de {:.2f}x{:.2f} e sua area é de {:.2f}m².'.format(lar, alt, area))
print('Você precisará de {:.2f} litros de tinta para pintar está parede!'.format(tinta))
