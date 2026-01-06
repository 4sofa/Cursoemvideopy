from math import factorial
from time import sleep
print('-='*20)
print(' '*2, 'Aplicativo para fatoriar numeros')
print('-='*20)
n = int(input('Digite um valor: '))
f = factorial(n)
a = n
print(f'Fatoriando...')
print(' ')
sleep(1)
while a != 1:
    print(f'{a}x', end='')
    a -= 1
    if a == 1:
        print(f'1', end='')
print(f'\nO resultado do fatorial de {n} é {f}')
