lista = []
maior = []
menor = []
for contagem in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {contagem}: ')))

print(f'Os valores da lista foram {lista}')

for pos, valores in enumerate(lista):
    if valores == max(lista):
        maior.append(pos)

    if valores == min(lista):
        menor.append(pos)

print(f'O menor valor foi {min(lista)} nas posições {menor}')
print(f'O maior valor foi {max(lista)} nas posições {maior}')
