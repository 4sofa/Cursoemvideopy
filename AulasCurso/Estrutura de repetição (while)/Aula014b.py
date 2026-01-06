idade = 1
pessoa = 1
nome = ''
while idade < 21:
    nome = str(input(f'Digite seu nome: ')).strip().capitalize()
    idade = int(input(f'{nome}. Digite sua idade: '))
    if idade < 21:
        print(f'Você tem {idade} anos. É menor de idade')
        pessoa += 1

if idade >= 21:
    print(f'Parabéns {nome}, você é maior de idade!')

print('Fim')
