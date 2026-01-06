galera = list()
dados = list()
for c in range(0,2):
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for n, i in galera:
    print(f'Nome: {n}, Idade: {i}')

for p in galera:
    print(p[1])
    