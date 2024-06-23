# isalnum – Verifique se todos os caracteres no texto são alfanuméricos
# isalpha – Verifique se todos os caracteres no texto são letras
# isascii – Verifique se a sequência é composta por todos os caracteres ASCII ou se a sequência estiver vazia também ret
# ornara true
# isdecimal – Verifique se todos os caracteres no objeto unicode são decimais
# isdigit – Verifique se todos os caracteres no texto são dígitos
# isidentifier – Verifique se a sequência é um identificador válido :: O método isidentifier () retornará True se a stri
# ng for um identificador válido, caso contrário, False. Uma sequência é considerada um identificador válido se contiver
# apenas letras alfanuméricas (a-z) e (0-9) ou sublinhados (_). Um identificador válido não pode começar com um número
# ou contem espaços.
# islower – Verifique se todos os caracteres do texto estão em minúsculas
# isnumeric – Verifique se todos os caracteres no texto são numéricos
# isprintable – Verifique se todos os caracteres no texto são imprimíveis
# isspace – Verifique se todos os caracteres no texto são espaços em branco
# istitle – Verifique se cada palavra começa com uma letra maiúscula
# isupper – Verifique se todos os caracteres do texto estão em maiúsculas

coisa = input('Digite qualquer coisa: ')
print('Qual o tipo primitivo de {}. '.format(coisa), type(coisa))
print('Os caracteres são numericos? ', coisa.isnumeric())
print('Só possui letras maiusculas? ', coisa.isupper())
print('é um numero ou uma letra do alfabeto? ', coisa.isalnum())
print('É um numero entre 0 e 9? ', coisa.isdecimal())
print('So possui letras minusculas? ', coisa.islower())
print('Somente possui espaços? ', coisa.isspace())
print('É imprimivel? ', coisa.isprintable())
print('É alfabetico? ', coisa.isalpha())
print('É alfanumerico? ', coisa.isalnum())
print('está capitalizada?', coisa.istitle())
