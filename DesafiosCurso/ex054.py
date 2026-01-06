# leia o ano de nascimento de sete pessoas
from datetime import date
date = date.today().year
maior = 0
menor = 0
for data in range(1, 7 + 1):
    a = int(input(f'A {data}° pessoa: '))
    idade = date - a
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'\033[m{maior} pessoas atingiram a maioridade')
print(f'{menor} pessoas não atingiram a maioridade')
