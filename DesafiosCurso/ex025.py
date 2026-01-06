nome = str(input('Digite seu nome completo: ')).strip().upper()
print('O seu nome tem Silva?\n{}'.format('SILVA' in nome.split()))
nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome tem Silva?\n{}'.format('SILVA' in nome.upper().split()))
