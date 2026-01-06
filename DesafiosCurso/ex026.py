letra = str(input('Digite uma frase: ')).strip().upper()
print('Na frase apareceu {} vezes a letra A.\n'
      'Ela apareceu pela primeira vez na posição {}.\n'
      'Ela apareceu pela ultima vez na posição {}.'.format(letra.count('A'), letra.find('A'), letra.rfind('A')))
