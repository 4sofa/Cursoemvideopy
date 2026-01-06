valor = int(input('Qual valor você quer sacar? R$'))

ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1
a = b = c = d = 0

while True:
    if valor >= ced50:
        valor -= ced50
        a += 1
    elif valor >= ced20:
        valor -= ced20
        b += 1
    elif valor >= ced10:
        valor -= ced10
        c += 1
        if valor == 0:
            break
    elif valor >= ced1:
        valor -= ced1
        d += 1
    if valor == 0:
        break
print('-'*40)
print(f'Voce sacou {a} cedulas de R$50')
print(f'Voce sacou {b} cedulas de R$20')
print(f'Voce sacou {c} cedulas de R$10')
print(f'Voce sacou {d} cedulas de R$1')
print('-'*40)
