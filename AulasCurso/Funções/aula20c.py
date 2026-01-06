def contador(*num):  # serve para desempacotar os dados
    print(num)
    tam = len(num)
    print(f'Nesta lista há {tam} valores')


contador(1, 2, 3, 4, 5)
contador(5, 6, 7, 8, 9)
contador(4, 8, 3) # a variavel NUM virou uma lista com todos os itens que eu passo através do parenteses do contador, pode-se manipular assim através de manipulação de listas os valores dentro
