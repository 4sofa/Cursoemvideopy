# Ler as partes da frase
frase = str(input('Digite alguma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('é um palindromo')
else:
    print('não é')
# confirmando se a palavra se repete


