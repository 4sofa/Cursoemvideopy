# Leia o peso e altura de uma pessoa
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2
if 10 <= imc < 18.5:
    print('Você esta abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal, parabens!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso, cuide-se melhor!')
elif 30 <= imc <= 40:
    print('Você está OBESO, cuide-se melhor!')
elif 40 < imc:
    print('Você está com obesidade morbida, busque tratamento!')
elif imc < 10:
    print('Valor invalido')
else:
    print('voce fez o impossivel')
