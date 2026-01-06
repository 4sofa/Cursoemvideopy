nome = str(input('Digite seu nome completo: ')).strip()
split = nome.split()
junto = ''.join(split)
print('{}\n{}\nSeu nome tem ao todo {} letras\nSeu primeiro nome é {} e ele tem {} letras.'.format(
    nome.upper(), nome.lower(), len(junto), split[0], len(split[0])))
# ou 
print('{}\n{}'.format(nome.find(' '), len(nome) - nome.count(' ')))
