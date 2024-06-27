sal = float(input('Qual o seu salario? '))
if sal > 1250.00:
    a = 0.10
    dez = sal * a
    aumento = sal + dez
    print('O aumento de 10%, fez seu salario subir para {:.2f}'.format(aumento))
if sal <= 1250.00:
    a = 0.15
    dez = sal * a
    aumento = sal + dez
    print('O aumento de 15%, fez seu salario subir para {:.2f}'.format(aumento))
