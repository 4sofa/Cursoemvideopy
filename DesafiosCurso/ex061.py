a1 = float(input('Digite um número: '))
razao = float(input('Digite a razão: '))
termos = 1
print(f'A PA do número {a1} com a razão {razao} é:')
while termos != 11:
    an = a1 + (termos - 1) * razao
    if termos != 10:
        print(f'{an}, ', end='')
    else:
        print(f'{an}.')
    termos += 1
