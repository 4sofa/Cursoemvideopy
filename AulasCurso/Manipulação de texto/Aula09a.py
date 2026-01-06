def frase():
    fr = str(input('Digite uma frase com menos de 12 letras: '))
    if len(fr) >= 12:
        print('Sua frase tem que ter menos de 12 caracteres')
    else:
        print('Sua frase foi,{}'.format(fr))


frase()
