# se carro.esquerda():              if carro.esquerda():
# bloco _V_                             bloco True
# senão:                             else:
# bloco _F_                             bloco False

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 5:
    print('Seu carro ta novinho!')
else:
    print('Seu carro ja ta velho!')

tempo = int(input('Quantos anos tem seu carro? '))
print('seu carro é novo'if tempo <= 3 else 'seu carro é velho')
