times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza-EC', 'São Paulo', 'Bahia', 'Cruzeiro', 'Atl São Paranaense',
         'RB Bragantino', 'Atl São-MG', 'Vasco da Gama', 'Juventude', 'Internacional', 'Corinthians', 'Criciúma',
         'Cuiabá', 'Vitória', 'Gremio', 'Fluminense', 'Atlêtico-GO')
print('Times do Brasileirao')
print('-'*40)
times_upper = tuple(team.upper() for team in times)
time = ''

while True:
    print('[ 1 ] Para mostrar os 6 primeiros colocados')
    print('[ 2 ] Para mostrar os 4 ultimos colocados')
    print('[ 3 ] Para mostrar os times em ordem alfabetica')
    print('[ 4 ] Escolha um time para mostrar sua posição na tabela')
    print('[ 5 ] Para mostrar todos os times na tabela')
    print('[ 6 ] Sair')
    opcao = int(input('Escolha uma opcao: '))
    if opcao == 1:
        print('-'*20)
        for primeiros in range(0, len(times[0:6])):
            print(f'{primeiros+1}° {times[primeiros]}')
            print('-'*20)
    if opcao == 2:
        print('-'*20)
        for ultimos in range(16, len(times)):
            print(f'{ultimos+1}° {times[ultimos]}')
            print('-'*20)
    if opcao == 3:
        print('-'*40)
        for e in sorted(times):
            print(e)
    if opcao == 4:
        print('-'*40)
        while True:
            print('Digite 0 para voltar ao menu')
            time = str(input('Escolha um time: ')).upper().strip()
            if time == '0':
                break
            if time not in times_upper:
                print('O time nao existe na tabela')
                print('-'*40)
            else:
                for f in times_upper:
                    print(f'O {time} esta em {times_upper.index(time)+1}° na tabela')
                    print('-'*40)
                    break
    if opcao == 5:
        print('-'*40)
        print('Tabela Brasileirão')
        print('-'*40)
        for g in range(0, len(times)):
            print(f'{g+1}° {times[g]}')
        print('-'*40)

    if opcao == 6:
        break
    else:
        while opcao > 6 or opcao < 1:
            print('Opção invalida!')
            opcao = int(input('Escolha uma opcao: '))
