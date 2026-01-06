mulheres = 0
homens = 0
maior = 0
while True:
    print('-='*20)
    print('cadastre uma pessoa')
    print('-='*20)
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
    print('-='*20)
    if sexo not in 'MmFf':
        print('Opção Invalida. Tente Novamente!')
        sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
    if sexo in 'Mm':
        homens += 1
    elif sexo in 'F':
        if idade < 20:
            mulheres += 1
    if idade >= 18:
        maior += 1
    usuario = str(input('Quer cadastrar mais alguem? [S/N] ')).strip().upper()[0]
    while usuario != 'S' and usuario != 'N':
        print('Opção Invalida. Tente Novamente!')
        usuario = str(input('Quer cadastrar mais alguem? [S/N] ')).strip().upper()[0]
    if usuario == 'N':
        break
    elif usuario == 'S':
        continue

print('-='*5, 'FIM DO PROGRAMA', '-='*5)
print(f'Total de pessoas com mais de 18 anos cadastradas: {maior}!')
print(f'Mulheres com menos de 20 anos cadastradas: {mulheres}!')
print(f'Homens cadastrados: {homens}!')
