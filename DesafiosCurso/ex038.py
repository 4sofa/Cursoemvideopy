from time import sleep

print('\033[34m-=-\033[m'*20)
print(' '*17, '\033[33mComparador de números\033[m')
print('\033[34m-=-\033[m'*20)
# Escreva dois números inteiros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
# Compare-os
# Mostre na tela se n1 é maior que n2
if n1 > n2:
    print('O primeiro número digitado é o maior')
elif n2 > n1:
    print('O segundo número digitado é o maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('\033[31mVocê fez cagada!\033[m')
