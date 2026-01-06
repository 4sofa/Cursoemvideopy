def ex004():
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

    coisa = input('\033[36;41mDigite qualquer coisa:\033[m ')
    print('\033[33mQual o tipo primitivo de {}.\033[m '.format(coisa), type(coisa))
    print('\033[34mOs caracteres são numericos?\033[m ', coisa.isnumeric())
    print('\033[35mSó possui letras maiusculas?\033[m ', coisa.isupper())
    print('\033[36mé um numero ou uma letra do alfabeto?\033[m ', coisa.isalnum())
    print('\033[37mÉ um numero entre 0 e 9?\033[m ', coisa.isdecimal())
    print('\033[32mSo possui letras minusculas?\033[m ', coisa.islower())
    print('\033[31mSomente possui espaços?\033[m ', coisa.isspace())
    print('\033[30mÉ imprimivel?\033[m ', coisa.isprintable())
    print('\033[33;45mÉ alfabetico?\033[m ', coisa.isalpha())
    print('\033[37;44mÉ alfanumerico?\033[m ', coisa.isalnum())
    print('\033[32;46mestá capitalizada?\033[m ', coisa.istitle())


ex004()
