import math
catadjacente = float(input('Digite o comprimento do cateto adjacente: '))
catoposto = float(input('Digite o comprimento do cateto oposto: '))
calculo = math.hypot(catadjacente, catoposto)
print('O comprimento da hipotenusa é: {:.2f}'.format(calculo))
