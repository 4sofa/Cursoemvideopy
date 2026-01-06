money = float(input('Quanto dinheiro você tem? R$'))
dol = money / 3.27
print('Com R${:.2f} você pode comprar US${:.2f} dolares!'.format(money, dol))
