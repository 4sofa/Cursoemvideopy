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

algo = input('Digite algo: ')
print(algo, 'É do tipo primitivo', type(algo))
print(algo,'Possui apenas números?', algo.isnumeric())
print(algo,'Possui apenas letras?', algo.isalpha())
print(algo,'Possui letras ou números?', algo.isalnum())
print(algo,'Possui números de 0 a 9?', algo.isdecimal())
print(algo,'Possui todos as palavras em minúsculo?', algo.islower())
print(algo,'Possui espaços apenas espaços em branco?', algo.isspace())
print(algo,'Possui apenas letras maiúsculas?', algo.isupper())
print(algo,'Possui a primeira palavra maiúscula e o restante minúsculas?',algo.istitle())


