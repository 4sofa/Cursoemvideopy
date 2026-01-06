soma = numeros = 0

n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    numeros += 1
    n = int(input('Digite um número [999 para parar]: '))

print(f'A soma de todos os valores foi {soma}\n'
      f'Foram digitados {numeros} números!')
