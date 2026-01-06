somaidade = 0
nmulher = 0
maiorh = 0
menor = 0
n = 0
velho = ''

for c in range(1, 4+1):
    print(f'---- {c}° Pessoa ----')
    nome = str(input(f'Nome: ')).strip().upper()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'M/F: '))

    # Soma de idade
    somaidade += idade

    # Quantas mulheres tem menos de 20 anos
    if sexo in 'Ff':
        if idade < 20:
            nmulher += 1

    # Nome do homem mais velho
    if c == 1 and sexo in 'Mm':
        maiorh = idade
        velho = nome

    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        velho = nome

# Media de idade
div = somaidade / 4
print(f'A média de idade do grupo é de {div:.0f} anos!')
if nmulher == 1:
    print(f'Tem {nmulher} mulher com menos de 20 anos!')
else:
    print(f'Tem {nmulher} mulheres com menos de 20 anos!')

print(f'O homem mais velho no grupo é o {velho}, e ele tem {maiorh} anos!')
