nome = str(input('Seu nome é Gustavo. Digite seu nome: ')).capitalize().strip()
name = nome.capitalize()
while nome != 'Gustavo':
    print(f'Seu nome não é {name}. Tente novamente.')
    nome = str(input('Seu nome é Gustavo. Digite seu nome: ')).capitalize().strip()
    name = nome.capitalize()

print(f'Parabéns, seu nome é {nome}!')

'''c = 0
while c < 10:
    print(f'C ainda nao chegou em 10. C = {c}')
    c += 1

print('C chegou em 10. C = 10')'''

numero = int(input('Digite um número inteiro menor que 100: '))
while numero <= 100:
    print(f'Número menor que 100. Número = {numero:}')
    numero = int(input('Digite um número: '))

print('Número maior que 100. Número = 100')
print('Parabéns')
