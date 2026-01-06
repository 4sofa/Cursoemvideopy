from time import sleep

# Valor a ser pago por um produto
print('='*15, 'LOJAS SOFA', '='*15)
produto = float(input('Valor do produto: R$'))
# Considerando o seu preço normal e condição de pagamento
print('-=-'*14)
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista, dinheiro/cheque 10% off')
print('[ 2 ] à vista no cartão, 5% off')
print('[ 3 ] em até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão, 20% de juros')
metodo = int(input('Escolha o metodo de pagamento: '))
print('-=-'*14)
print('PROCESSANDO...')
sleep(2)
if metodo == 1:
    valor = produto - (produto*0.10)
    print(f'O valor do seu produto será de R${valor:.2f}')
elif metodo == 2:
    valor = produto - (produto*0.05)
    print(f'O valor do seu produto será de R${valor:.2f}')
elif metodo == 3:
    print(f'O valor do seu produto será de R${produto:.2f}, em 2x sem juros!')
elif metodo == 4:
    parcelas = int(input('Número de parcelas: '))
    valor = produto + (produto*0.20)
    valorparcelado = valor / parcelas
    print(f'O valor do seu produto será de R${valorparcelado:.2f}, com {parcelas:.0f}x'
          f' de R${valorparcelado:.2f} com juros!\nSua compra de R${produto:.2f} custará R${valor:.2f}')
elif metodo > 4 or metodo < 1:
    print('\033[31mMétodo inválido. Tente novamente!\033[m')
