sal = float(input('Qual o seu salario? R$'))
if sal > 1250.00:
    new = sal + (sal * 10 / 100)
    print('O aumento de 10%, fez seu salario subir para R${:.2f}'.format(new))
if sal <= 1250.00:
    new = sal + (sal * 15 / 100)
    print('O aumento de 15%, fez seu salario subir para R${:.2f}'.format(new))
