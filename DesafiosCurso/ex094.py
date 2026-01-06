def ex094():
    somaidade = 0
    m = 0
    pessoas = list()
    mulheres = list()
    acimamediafem = list()

    while True:
        cadastro = {'nome': str(input('Nome: ')).capitalize().strip(), 'idade': int(input('Idade: ')),
                    'sexo': str(input('Sexo: [M/F] ')).upper().strip()[0]}
        pessoas.append(cadastro.copy())
        continuar = str(input('Quer continuar? S/N: ')).strip().upper()[0]
        while continuar not in 'SN':
            continuar = str(input('Digite novamente! S/N: ')).strip().upper()[0]
        if continuar in 'S':
            continue
        elif continuar in 'N':
            break

    npessoas = len(pessoas)
    print('idades: ', end='')
    for e in range(npessoas):
        print(f'{pessoas[e]["idade"]}', end='--')   # exibir todas as idades
        somaidade += (pessoas[e]["idade"])
        if pessoas[e]["sexo"] in 'F':
            mulheres.append(pessoas[e]["nome"])
            m += 1

    mediareal = somaidade / len(pessoas)

    amf = 0
    for d in range(npessoas):
        if pessoas[d]["idade"] > mediareal and pessoas[d]["sexo"] in 'F':
            acimamediafem.append(pessoas[d])
            amf += 1

    acimamediamasc = list()
    amM = 0
    for k in range(npessoas):
        if pessoas[k]["idade"] > mediareal and pessoas[k]["sexo"] in 'M':
            acimamediamasc.append(pessoas[k])
            amM += 1


    print('')
    print('-='*20)
    print(f'- O grupo tem {len(pessoas)} pessoas.')  # USE LEN() PARA DEFINIR NUMERO DE PESSOAS CADASTRADAS
    # Todas mulheres registradas
    print(f'- As mulheres são: ', end='')
    for c in range(m):
        if c != m - 1:
            print(f'{mulheres[c]} e', end=' ')
        else:
            print(f'{mulheres[c]}')

    # Média idade
    print(f'- A idade média é: {mediareal}')

    # Acima da média
    print(f'- As pessoas com idade acima da média são:\n')

    print(f'nome = {acimamediafem[0]["nome"]}; sexo: {acimamediafem[0]["sexo"]}; idade = {acimamediafem[0]["idade"]}.\n')
    print(f'nome = {acimamediamasc[0]["nome"]}; sexo: {acimamediamasc[0]["sexo"]}; idade = {acimamediamasc[0]["idade"]}.')

    print('FIM')


ex094()
