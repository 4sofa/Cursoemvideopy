a = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))
print('-'*20)
tupla = (n1, n2, n3, n4)
print(f'Você digitou os seguintes valores: {tupla}')
print(f'O maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')
print(f'Apareceu o numero nove, {tupla.count(9)} vezes')
if tupla.count(3) == 0:
    print('O numero 3 não foi digitado em nenhuma posição')
else:
    print(f'o numero 3 apareceu na {tupla.index(3)+1}° posição')
print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        a += 1
        print(c, end=' ')
print(f'\nHouveram {a} numeros pares digitados')
