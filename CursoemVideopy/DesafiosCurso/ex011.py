lar = int(input('Coloque em metros a largura da sua parede: '))
alt = int(input('Coloque em metros a altura da sua parede: '))
area = lar * alt
tinta = area / 2
print('Você precisará de {} litros de tinta para pintar a parede!'.format(tinta))
