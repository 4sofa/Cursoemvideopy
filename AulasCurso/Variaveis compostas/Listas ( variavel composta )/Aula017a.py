valores = list(range(4, 11, 2))
print(valores)
print(f'a largura da lista é de {len(valores)} algarismos')
lista = [5, 8, 3, 2, 8, 9, 2, 0]
# Comando para ordenar a lista em ordem crescente
lista.sort()
print(f'\nLista em ordem crescente \n{lista} ')

# Comando para ordenar a lista em ordem decrescente
lista.sort(reverse=True)
print(f'\nLista em ordem decrescente \n{lista}')
