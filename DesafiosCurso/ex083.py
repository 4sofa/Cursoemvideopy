expressao = list()

expressao.append(str(input('Digite a expressão: ')))

if expressao[0].count('(') == expressao[0].count(')'):
    print('expressão valida')
else:
    print('Expressão invalida')
