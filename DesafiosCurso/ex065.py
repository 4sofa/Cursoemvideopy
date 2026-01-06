maior = menor = media = soma = vezes = 0
continuar = 'S'

while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    vezes += 1
    if vezes == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma / vezes
print(f'A media entre os valores foi {media}')
print(f'O maior valor lido foi {maior}')
print(f'O menor valor lido foi {menor}')
