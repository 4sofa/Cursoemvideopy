# leia a data de nascimento
from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
# Mostre a categoria onde ele se encontra
today = date.today().year
idade = today - nascimento
print(f'Você tem {idade} anos')
if 1 <= idade <= 9:
    print('\033[34mMIRIM-MIRIM-\033[m'*4)
    print(' '*12, '\033[34mSua categoria é MIRIM!\033[m')
    print('\033[34mMIRIM-MIRIM-\033[m'*4)
elif 10 <= idade <= 14:
    print('\033[35mINFANTIL-INFANTIL-\033[m' * 4)
    print(' '*18, '\033[35mSua categoria é INFANTIL!\033[m')
    print('\033[35mINFANTIL-INFANTIL-\033[m' * 4)
elif 15 <= idade <= 19:
    print('\033[32mJUNIOR-JUNIOR-\033[m' * 4)
    print(' '*14, '\033[32mSua categoria é JUNIOR\033[m')
    print('\033[32mJUNIOR-JUNIOR-\033[m' * 4)
elif 20 <= idade < 25:
    print('\033[33mSENIOR-SENIOR-\033[m' * 4)
    print(' '*14, '\033[33mSua categoria é SENIOR\033[m')
    print('\033[33mSENIOR-SENIOR-\033[m' * 4)
elif 26 <= idade <= 100:
    print('\033[1mMASTER-MASTER-\033[m' * 4)
    print(' '*14, '\033[1mSua categoria é MASTER\033[m')
    print('\033[1mMASTER-MASTER-\033[m' * 4)
else:
    print('\033[31mERROR-ERROR-\033[m' * 6)
    print(' '*14, f'\033[31mVocê não tem {idade} anos, corrija o valor\033[m')
    print('\033[31mERROR-ERROR-\033[m' * 6)
