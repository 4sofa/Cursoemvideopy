nome = str(input('Digite seu nome completo: ')).strip().upper()
separa = nome.split()
print('Primeiro nome: {}'.format(separa[0]))
print('Segundo nome: {}'.format(separa[-1]))
# ou
print('Segundo nome: {}'.format(separa[len(separa)-1]))
