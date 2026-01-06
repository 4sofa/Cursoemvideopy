# Listas []
# As listas são MUTAVEIS ex:
lista = ['Pao', 'Açucar', 'Leite']

print(f'Lista antes {lista}')

# Este comando altera um item na lista
lista[2] = 'Café'

print(f'\nlista depois {lista}')

# Este comando adiciona um item na lista
lista.append('Arroz')

# Este comando insere um item a lista na posição escolhida
lista.insert(0, 'Cachorro quente')
print(f'\nlista bem depois {lista}')

# Comando para eliminar itens da lista por numeração
del lista[1]
print(f'\nLista sem pao {lista}')

# Comando para eliminar itens da lista por numeração OU para eliminar o ultimo item da lista
lista.pop(3)
print(f'\nLista sem arroz {lista}')

# Comando para eliminar itens por nome da lista 'Detalhe: ele so exclui o primeiro valor que encontrar'
lista.remove('Cachorro quente')
print(f'\nLista sem cachorro quente {lista}')

# eliminar o ultimo item da lista
lista.pop()
print(f'\nLista sem café {lista}')

if 'Açucar' in lista:
    print('Na lista há açucar')
else:
    print('Na lista não tem açucar')
