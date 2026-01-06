s = 0
quant = 0
print('Digite [999] para parar!')
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s += n
    quant += 1

print(f'A soma de todos os valores foi {s}')
print(f'Você digitou {quant} valores!')
print('fim do programa')
