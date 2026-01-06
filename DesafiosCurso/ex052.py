# numeros primos são aqueles somente divisiveis por 1 ou por ele mesmo
n = int(input('Digite um número: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\033[m\nO número {n} foi dividido {div} vezes')
if div == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
