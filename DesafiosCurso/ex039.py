from datetime import date
# Faça um programa que leia o ano de nascimento de um jovem e
# informe de acordo com sua idade
nascimento = int(input('Digite seu ano de nascimento: '))
today = date.today()

idade = today.year - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, today.year))
if idade < 18:
    falta = 18 - idade
    print('Daqui {} anos, você vai se alistar!'.format(falta))
    print('Seu alistamento será em {}'.format(today.year + falta))
elif idade == 18:
    print('é hora de se alistar')
elif idade > 18:
    c = idade - 18    # quanto tempo falta
    print('Ja passou {} anos do tempo do alistamento'.format(c))
