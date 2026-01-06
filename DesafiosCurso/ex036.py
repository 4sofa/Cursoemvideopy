from time import sleep

print('\033[33m-=-\033[m'*20)

print(' '*18, '\033[34mEmpréstimo Bancário\033[m')

print('\033[33m-=-\033[m'*20)

# Valor da casa
valorcasa = float(input('Digite o valor da casa que você quer comprar: '))
# Salário do comprador
salario = float(input('Digite o seu sálario: '))
# Em quantos anos ele vai pagar
pagaranos = int(input('Digite em quantos anos pagará: '))

# Calcule o valor da prestação mensal
# Ela não pode exceder 30% do salário

prestacao = valorcasa / (pagaranos * 12)
trintaporcento = salario * 0.30

print('\033[33mPROCESSANDO...\033[m')
sleep(2)

# Se exceder sera negado
if prestacao > trintaporcento:
    print('\033[31mERRO-ERRO-\033[m'*10)

    print(' '*8, '\033[31mSeu empréstimo foi negado! '
                 'Sua parcela de R${:.2f} excede 30% do valor do salário de R${:.2f}\033[31m'
          .format(prestacao, salario))

    print('\033[31mERRO-ERRO-\033[m'*10)
else:
    print('\033[32mAPROVADO-APROVADO-\033[m'*5)
    print(' '*5, '\033[32mSeu empréstimo de R${:.2f} por foi aprovado,\033[m'
          '\033[32mvocê pagará R${:.2f} por mês!\033[m'.format(valorcasa, prestacao))
    print('\033[32mAPROVADO-APROVADO-\033[m'*5)
