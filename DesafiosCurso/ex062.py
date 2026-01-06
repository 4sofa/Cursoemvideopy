a1 = float(input('Digite um número: '))
razao = float(input('Digite a razão: '))
termos = 1
an = 0
mais = 1
print(f'A PA do número {a1} com a razão {razao} é:')
while termos != 11:
    an = a1 + (termos - 1) * razao
    if termos != 10:
        print(f'{an}, ', end='')
    else:
        print(f'{an}.')
    termos += 1

mais = int(input('Digite quantos termos quer: [0 para parar]: '))
while mais != 0:
    for i in range(termos, termos + mais):
        an = a1
        ann = a1 + (i - 1) * razao
        print(f'Este é o {i}° termo da PA: {ann}')
    termos += 1
    mais = int(input('Digite quantos termos quer: [0 para parar]: '))

print('PROGRAMA ENCERRADO!')
