# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência ou função pow()
# // Divisão Inteira
# % Resto da Divisão
# Ordem de Precedência (1. ().)  (2. **.) (3. *, /, //, %.) (4. +, -.)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 - n2
multi = n1 * n2
di = n1 // n2
dv = n1 / n2
expo = n1 ** n2
# o {:.3f} significa 3 casa flutuantes apos a virgula ou ponto. O (\n) significa nova linha.
# O end='' significa vazio
print('A soma vale {}, \n a subtração vale {} e a multi {}. '.format(s, m, multi), end='')
print('A divisão inteira vale {}, a divisão vale {:.3f} e a potência vale {}'.format(di, dv, expo))
