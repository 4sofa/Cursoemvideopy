# usar len para determinar quantos valores na lista
# usar o laço para varrer a lista e determinar quais são os maiores valores
from ex096 import calculando
from ex097 import mostrarTexto
from time import sleep

def numeroMaior():
    listaNumeros = []
    for listas in range(5):
        numerais = int(input('Digite um número:  '))
        listaNumeros.append(numerais)
    print('-='*20)
    print(f'Analisando os valores passados...') 
    for i in range(len(listaNumeros)):
        sleep(0.3)
        if i == len(listaNumeros) - 1:
            print(f'{listaNumeros[i]}', flush=True)
        else:    
            print(f'{listaNumeros[i]} ', end='', flush=True)
    calculando('Verificando o maior')
    listaNumeros.sort(reverse=True)
    print(f'O maior número encontrado foi {listaNumeros[0]}')
    print('-='*20)

mostrarTexto('Descobrindo qual o maior número')

numeroMaior()



# ou pode ser feito desta forma
# usar len para determinar quantos valores na lista
# usar o laço para varrer a lista e determinar quais são os maiores valores
#from ex096 import calculando
#from ex097 import mostrarTexto
#from time import sleep

##def numeroMaior(* listaNumeros):

#    i = 0
#    cont = maior = 0
#    print('-='*20)
#    print(f'Foram passados {len(listaNumeros)} valores')
#    print(f'Analisando os valores passados...') 
#    for valor in listaNumeros:
#        sleep(0.3)
#        if i == len(listaNumeros) - 1:
#            print(f'{valor}', flush=True)
#        else:    
#            print(f'{valor} ', end='', flush=True)
#        i += 1
#        if cont == 0:
#            maior = valor
#        else:
#            if valor > maior:
#                maior = valor
#        cont += 1

#    calculando('Verificando o maior')
#    print(f'O maior número encontrado foi {valor}')
#    print('-='*20)

#mostrarTexto('Descobrindo qual o maior número')

#numeroMaior(1, 2, 3, 4, 5, 6, 7, 8)


# ou tambem usando max()

# usar len para determinar quantos valores na lista
# usar o laço para varrer a lista e determinar quais são os maiores valores
#from ex096 import calculando
#from ex097 import mostrarTexto
#from time import sleep

#def numeroMaior(* listaNumeros):
#    i = 0
#    print('-='*20)
#    print(f'Foram passados {len(listaNumeros)} valores')
#    print(f'Analisando os valores passados...') 
#    for valor in listaNumeros:
#       sleep(0.3)
#        if i == len(listaNumeros) - 1:
#            print(f'{valor}', flush=True)
#        else:    
#            print(f'{valor} ', end='', flush=True)
#        i += 1
        

#    calculando('Verificando o maior')
#    print(f'O maior número encontrado foi {max(listaNumeros)}')
#    print('-='*20)

#mostrarTexto('Descobrindo qual o maior número')

#numeroMaior(1, 2, 3, 4, 5, 6, 7, 8)