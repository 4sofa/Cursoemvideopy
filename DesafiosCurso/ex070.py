total = 0
preco1000 = 0
maior = 0
menor = 0
a = 0
parar = ''
b = ''
while True:
    print('-'*20, 'CADASTRE UM PRODUTO', '-'*20)
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    print('-'*20)
    total += preco
    a += 1
    if preco >= 1000.00:
        preco1000 += 1
    if a == 1:
        menor = preco
        b = nome
    else:
        if preco < menor:
            menor = preco
            b = nome
    parar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while parar != 'S' and parar != 'N':
        print('Opção Invalida. Tente Novamente!')
        parar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if parar == 'N':
        break

print('-'*20, 'Fim do programa', '-'*20)
print(f'O total gasto nas compras foi de R${total:.2f}')
print(f'( {preco1000} ) produtos custam mais de R$1000.00')
print(f'O produto mais barato foi {b} custando R${menor:.2f}')
