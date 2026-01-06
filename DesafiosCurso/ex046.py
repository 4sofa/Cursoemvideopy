# Exercicio 46
# contagem regressiva na tela com cooldown de 1 segundo

from time import sleep
for cooldown in range(10, -1, -1):
    print(f'Faltam {cooldown} segundos para explosão!')
    sleep(1)
print('\033[31mKABUM! Os fogos explodiram.\033[m')
