sexo = ''
masculino = 0
feminino = 0
print('Digite 0 para encerrar o programa.')
while sexo != '0':
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida. Tente novamente.')
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1

print(f'Foram registrados {masculino} homens e {feminino} mulheres.')
