n = int(input('Digite um numero: '))
contagem = 0
t2 = 1
t3 = 1
print(f'\nOs primeiros {n} da sequencia de fibonacci são:')
print('-=' * 20)
print(f'{contagem} --> {t2} --> {t2} --> ', end='')
while n - 3 != contagem:
    t = t2 + t3
    print(f'{t} --> ', end='')
    t2 = t3
    t3 = t
    contagem += 1

print('FIM')
print('-=' * 20)
