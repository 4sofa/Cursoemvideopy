nome = str(input('Qual o seu nome? ')).capitalize().split()
idade = int(input('Qual a sua idade? '))
sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
if sexo not in 'MF':
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
else:
    tupla = (nome, idade, sexo)
    print('-'*40)
    for pos, c in enumerate(tupla):
        if pos == 0:
            print(f'Seu nome é {c}')
        elif pos == 1:
            print(f'Sua idade é {c}')
        elif pos == 2:
            print(f'Seu sexo é {c}')

# ou
    del tupla
    print('-'*40)
    print('Separação de dados:')
    print('-'*40)
    tupla = (f'Seu nome é {nome}', f'Sua idade é {idade}', f'Seu sexo é {sexo}')
    for pos, c in enumerate(tupla):
        if pos == 0:
            print(c)
        elif pos == 1:
            print(c)
        elif pos == 2:
            print(c)
