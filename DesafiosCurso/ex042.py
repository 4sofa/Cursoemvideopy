seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
# a soma do seguimento 1 e 2 tem q ser maior q o seguimento 3 para formar um triangulo
if seg3 < seg1 + seg2 and seg1 < seg3 + seg2 and seg2 < seg1 + seg3:
    print('\033[33mPode formar um triangulo\033[m', end='\n')
    if seg1 == seg2 == seg3:
        print('Este é um triangulo Equilátero!')
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        print('Esté é um triangulo Isósceles!')
    elif seg1 != seg2 != seg3:
        print('Este é um triangulo Escaleno')
else:
    print('Nao pode formar um triangulo')
