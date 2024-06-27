# Pergunte a distância em KM
# Calcule o preço da passagem cobrando 0,50 por KM para até 200KM
# e 0,45 para viagens mais longas

distancia = int(input('Qual a distancia que você percorreu em Km? '))
preco = 0.50 * distancia
preco2 = 0.45 * distancia
if distancia <= 200:
    print('O preço da passagem foi {} para {}km.'.format(preco, distancia))
elif distancia > 200:
    print('O preço da passagem foi {} para {}km.'.format(preco2, distancia))
