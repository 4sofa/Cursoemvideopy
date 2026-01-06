n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))
lista = [n1, n2, n3]
# Este sort significa que vai organizar a lista em ordem crescente
lista.sort()
# ou print('{}'.format(max(lista)))
# print('{}'.format(min(lista)))
print('Maior valor {}\nMenor valor {}'.format(lista[2], lista[0]))
# 2° método
# verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O menor valor é: {}'.format(menor))
# verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é: {}'.format(maior))
