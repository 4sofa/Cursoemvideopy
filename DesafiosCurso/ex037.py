print("\033[31m-=-\033[m"*20)
print(' '*18, 'BASES DE CONVERSÃO')
print("\033[31m-=-\033[m"*20)

# Lendo número inteiro
ninteiro = int(input('Escolha um número inteiro: '))
# Escolher base de conversão do número
print('\033[32m[ 1 ] converter para binário\033[m')
print('\033[33m[ 2 ] converter para hexadecimal\033[m')
print('\033[34m[ 3 ] converter para octal\033[m')

converta = int(input('Sua opção: '))

if converta == 1:
    binario = bin(ninteiro)  # or bin(ninteiro)[2:]
    print('Seu número em binário é {}'.format(binario[2:]))

elif converta == 2:
    hexadecimal = hex(ninteiro)
    print('Seu número em hexadecimal é {}'.format(hexadecimal[2:]))

elif converta == 3:
    octal = oct(ninteiro)
    print('Seu número em octal é {}'.format(octal[2:]))
else:
    print('\033[31mERRO-ERRO-\033[m'*5)
    print(' '*7, '\033[31mOPÇÃO INVÁLIDA. Tente Novamente!\033[m')
    print('\033[31mERRO-ERRO-\033[m'*5)
