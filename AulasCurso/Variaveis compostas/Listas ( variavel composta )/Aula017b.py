num = [1, 1, 3, 6, 9, 2, 2, 2]
while True:
    num.remove(2)
    if 2 not in num:
        break
print(num)
# ou

num2 = [1, 1, 3, 6, 9, 2, 2, 2]
while 2 in num2:
    num2.remove(2)
print(num2)

# ou

num3 = [1, 1, 3, 6, 9, 2, 2, 2]
for c in range(0, len(num3)):
    if 2 in num3:
        num3.remove(2)
print(num3)

valores2 = []
for valor in range(0, 5):
    valores2.append(valor)

print(valores2)

valores3 = [1, 7, 5, 3, 2, 8]

for pos, v in enumerate(valores3):
    print(f'O {pos+1}° valor desta lista é {v}')

aaaa = list()

for cont in range(0, 5):
    aaaa.append(int(input('Digite um valor: ')))

aaaa.sort()
print(f'{aaaa}')
