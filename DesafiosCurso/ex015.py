km = float(input('Digite a quantidade de Kilometros rodados: '))
dias = int(input('Digite a quantidade de dias rodados: '))
precokm = 0.15 * km
precodias = 60 * dias
total = precokm + precodias
print('O total a pagar sabendo que {} dias e {} km foram gastos é de R${:.2f}.'.format(dias, km, total))
