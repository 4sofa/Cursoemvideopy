reais = float(input('Coloque o preço do produto para adicionar o desconto: R$'))
desconto = reais * 0.05
preco = reais - desconto
# preco: float = reais - desconto ( este codigo também funciona e ele indica numero com virgula por conta do float)
print('Seu produto de R${:.2f}, agora com desconto de 5% vai custar R${:.2f}!'.format(reais, preco))
