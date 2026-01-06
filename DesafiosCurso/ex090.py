dados = {'nome': str(input('Digite seu nome: '))}
dados['media'] = float(input(f'Media de {dados["nome"]}: '))
print(f'Seu nome é {dados["nome"]}')
print(f'A media de {dados["nome"]} é {dados["media"]}')
if dados["media"] >= 6:
    print(f'Parabens, sua media foi {dados["media"]}, voce foi'
          f'aprovado!')
else:
    print(f'Sua média foi {dados["media"]}, voce foi reprovado!')
