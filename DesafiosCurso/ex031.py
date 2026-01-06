# Pergunte a distância em KM
# Calcule o preço da passagem cobrando 0,50 por KM para até 200KM
# e 0,45 para viagens mais longas

distancia = float(input('Qual a distancia que você percorreu em Km? '))
# if distancia <= 200:
#    preco = 0.50 * distancia
#    print('O preço da passagem foi {} para {}km.'.format(preco, distancia))
# elif distancia > 200:
#    preco2 = 0.45 * distancia
#    print('O preço da passagem foi {} para {}km.'.format(preco2, distancia))

# OU
preco = distancia * 0.50 if distancia < 200 else distancia * 0.45
print(preco)
