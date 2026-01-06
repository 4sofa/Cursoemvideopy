from datetime import date
info = {'nome': str(input('Digite seu nome: ')).title().strip(),
        'idade': int(input('Digite seu ano de nascimento: ')),
        'ctps': int(input('Carteira de trabalho (digite 0 caso não tenha): '))}
aposenta = 0
if info['ctps'] != 0:
    info['contratado'] = int(input('Ano de contratação: '))
    info['salario'] = float(input('Salário: R$'))
    aposenta = info["idade"] + (35 - (date.today().year - info['contratado']))
info["idade"] = date.today().year - info["idade"]


print(f'O nome tem o valor {info["nome"]}')
print(f'Idade tem o valor {info["idade"]}')
print(f'ctps tem o valor {info["ctps"]}')
if info["ctps"] != 0:
    print(f'contratação tem o valor {info["contratado"]}')
    print(f'salário tem o valor {info["salario"]:.2f}')
    print(f'aposentadoria tem o valor {aposenta}')
