#  \033[style; text ;back
# PADRÃO ANSI
# styles: 0 = none; 1 = bold (negrito); 4 = underline; 7 = negative
# text: 30 = branco; 31 = vermelho; 32 = verde; 33 = amarelo; 34 = azul; 35 = roxo; 36 = azul claro; 37 = cinza
# back: 40 = branco; 41 = vermelho; 42 = verde; 43 = amarelo; 44 = azul; 45 = roxo; 46 = azul claro; 47 = cinza
nome = 'Gustavo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, eu me chamo {}{}{}\033[m'.format(cores['amarelo'], nome, cores['limpa']))
