while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero < 0 or numero > 20:
        print('Tente novamente.')
    else:
        tupla = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
                 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
        print(f'Voce digitou o numero {tupla[numero]}')
        print('-'*40)
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if continuar not in 'SN':
            continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'N':
            break
