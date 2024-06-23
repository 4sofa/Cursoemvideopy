reais = float(input('Coloque o preço do produto para adicionar o desconto: '))
desconto = reais * 0.05
preco = reais - desconto
# preco: float = reais - desconto ( este codigo também funciona e ele indica numero com virgula por conta do float)
print('Seu produto de {:.2f} reais, agora com desconto de 5% custa {:.2f} reais!'.format(reais, preco))
