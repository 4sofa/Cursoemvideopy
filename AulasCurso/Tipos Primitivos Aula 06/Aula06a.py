# type usado para descobrir a classe do valor (int, str, float, bool etc
# print(type(n1))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# {} neste caso foi usado para alocar as variaveis n1, n2, e s, através do comando .format
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
