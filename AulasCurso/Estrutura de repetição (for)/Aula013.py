# laço (variavel de controle) no invertalo(numero do intervalo ex: 1, 10)
# for (varivael de controle) in range(1, 10)
#   (comandos)
# for c in range(6, 0, -1): ele conta do numero 6 até o numero 1 pq o -1 é menos uma casa
# caso fosse (0, 6, 2) ele pularia de duas em duas casas
#   print(c)

# nome = str(input('Digite seu nome: ')).upper()
# for a in range(0, 3):
#    if nome == 'GUSTAVO':
#        print(f'Olá {nome}')
#    else:
#        print('Oi')

# for c in range(0, 10, 2):
#     print(f'{c}')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if i > f:
    for e in range(i, f - 1, p):
        print(e)

else:
    for d in range(i, f + 1, p):
        print(d)

print('FIM')
