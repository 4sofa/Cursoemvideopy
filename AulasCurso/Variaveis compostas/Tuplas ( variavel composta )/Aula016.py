# Tuplas (variaveis compostas)
# TUPLAS SAO IMUTAVEIS

# TUPLAS
# lanche = 'hamburguer', 'suco', 'pizza', 'pudim', 'batatafrita'
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batatafrita')


# Listas
# lanche = ['hamburguer', 'suco', 'pizza', 'pudim', 'batatafrita',]

# Dicionario
# lanche = {'hamburguer','suco','pizza','pudim','batatafrita'}
print('-'*40)
print(' '*10, 'Aula016 - Tuplas')
print('-'*40)

pessoas = ('Maria', 'Helena', 'João', 'Carlos', 'Joaquim')
for c in range(0, len(lanche)):
    print(f'{pessoas[c]}. Eu vou comer {lanche[c]}')

print('-'*40)
print(' '*7, 'Separando as tuplas...')
print('-'*40)
for c in lanche:
    print(f'Eu vou comer {c.capitalize()}')

print('-'*40)
print(' '*7, 'Separando as tuplas...')
print('-'*40)
for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c.capitalize()} na posição {pos+1}')
    if c == 'suco':
        print(' ')
        print(f'A posição do suco é {pos+1}')
        print(' ')
print('-'*40)
print('Organizado em crescente do alfabeto')
print(sorted(lanche))
print('-'*40)
print('Juntando as tuplas')
a = (1, 2, 3, 4, 5, 8)
b = (6, 7, 8, 9, 10)
c = a+b
d = b+a
print(c)
print(d)
print(f'Quantas vezes aparece o numero 5? {c.count(5)}')
print(f'Quantos numeros tem na tupla? {len(c)}')
print(f'Em que posição esta o 8? {c.index(8)}')
