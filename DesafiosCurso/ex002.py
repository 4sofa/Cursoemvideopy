def ex002():
    nome = input('\033[7;34;40mQual é o seu nome?\033[m \033[m')
    # .format(nome)) é usado para formatar
    # uma variavel dentro dos conchetes
    print('\033[32mÉ um prazer te conhecer,\033[m \033[33m{}\033[m!'.format(nome))


ex002()
