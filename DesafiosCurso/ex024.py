nome = str(input('Digite o nome de uma cidade: ')).strip().upper()
print('O nome da sua cidade começa com santo?\n{}'.format(nome.startswith('SANTO')))
# ou

cidade = str(input('Digite o nome da sua cidade: ')).strip().upper().split()
print('O nome da sua cidade começa com santo?\n{}'.format('SANTO' in cidade[0]))
