a = [2, 3, 4, 7]
# Com ligação das listas b = a
b = a
b[2] = 8
print('Com ligação')
print(f'lista A: {a}')
print(f'Lista B: {b}\n')

# Sem ligação das listas b = a[:]

c = a[:]
c[2] = 7
print('Sem ligação (COPIA)')
print(f'lista A: {a}')
print(f'Lista C: {c}')
