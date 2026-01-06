# pessoas = [[str(input('Qual o seu nome? ')), int(input('Digite sua idade: '))]]
# print(pessoas)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print('Nomes       Idade')
for p in galera:
    print(f' {p[0]:<10} ', end='')
    print(f'{p[1]:>5}')
