palavras = ('aprendEr', 'programar', 'linguagem', 'python',)
for p in palavras:
    print(f'\nA palavra {p} tem as vogais:', end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras.upper(), end=' ')
print('\nfim do programa')
