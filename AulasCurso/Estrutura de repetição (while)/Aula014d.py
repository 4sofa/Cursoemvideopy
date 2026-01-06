
'''c = 0
while c < 10:
    print(f'C ainda nao chegou em 10. C = {c}')
    c += 1

print('C chegou em 10. C = 10')

numero = 0
while numero <= 100:
    numero = int(input('Digite um número inteiro menor que 100: '))
    print(f'Número menor que 100. Número = {numero}')
    numero = int(input('Digite um número: '))

print('Número maior que 100. Número = 100')
print('Parabéns')'''

r = 'S'
while r == 'S':
    numero = int(input('Digite um número inteiro: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()

print('Fim')