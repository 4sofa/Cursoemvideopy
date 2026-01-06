nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Gabriel':
    print('Que nome maravilhoso você tem!')
else:
    print('Que nome estranho você tem.')
print('Bom dia {}'.format(nome))
