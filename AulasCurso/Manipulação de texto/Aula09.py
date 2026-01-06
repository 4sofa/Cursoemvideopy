from random import choice

# fatiamento de strings, se usa conchetes para selecionar
# [começo, fim, numero de casas a pular]
# o número do caracter da variavel ou string
# print(a[0:21])
# o 2 adicionado por ultimo significa que ele pulará de 2 em 2
# print(a[0:21:2])
# print(a[:5])
# print(a[15:])
# print(a[9::3])
bb = 'Curso em Video Python'
repla = bb.replace('Video', 'Aula')


def b(aa):
    sta: bool = 'Curso' in aa
    return sta


resultado_b = b(bb)
frase = bb.count('o', 0, 18)
aaa = repla.upper()
bbb = repla.lower()
ccc = aaa.capitalize()
titulo = ccc.title()
avr = '   Frase inutil   '
avrr = avr.strip()
avrrr = avr.rstrip()
avrrrr = avr.lstrip()
split = bb.split()
separa = choice(split)
junta = ''.join(split)
fatia = bb[3]
print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(
    frase, resultado_b, repla, aaa, bbb, ccc, titulo, avrr, avrrr, avrrrr, separa, junta, fatia, split))
print('12'.split())
print(separa)
