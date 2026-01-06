# Faça um programa que leia o nome de 5 pessoas
maior = 0
menor = 0
for c in range(1, 5+1):
    peso = float(input(f'Digite o peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if menor > peso:
        menor = peso

print(f'O maior peso é {maior:.2f}KG')
print(f'O menor peso é {menor:.2f}KG')
