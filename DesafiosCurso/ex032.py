# calculo ano bissexto
from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar seu ano: '))
if ano == 0:
    ano = date.today().year   # comando para pegar o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # o simbolo % é resto da divisão, o simbolo != é diferente
    print('Ele é')
else:
    print('Ele não é')
