seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
# a soma do seguimento 1 e 2 tem q ser maior q o seguimento 3 para formar um triangulo
if seg3 < seg1 + seg2 and seg1 < seg3 + seg2 and seg2 < seg1 + seg3:
    print('\033[33mPode formar um triangulo\033[m')
else:
    print('\033[31mNão pode formar um triangulo\033[m')
