import time
import sys

def calculando(frase):
    for i in range(0, 2):
        print(f'{frase} (\)', end='\r') # \r sobrescreve o TEXTO no terminal
        time.sleep(0.2)
        print(f'{frase} (|)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (/)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (-)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (\)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (|)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (/)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (-)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (\)', end='\r')
        time.sleep(0.2)
        print(f'{frase} (|)', end='\r')
        time.sleep(0.2)
    sys.stdout.write("\033[KConcluido!\n")

def mostraLinha(msg1):
    print('-'*30)
    print(f'     {msg1}')
    print('-'*30)


time.sleep(2)
def calculoArea(LarguraM, ComprimentoM):
    area = LarguraM * ComprimentoM
    calculando('Finalizando')
    print(f'A área de um Terreno {LarguraM}x{ComprimentoM} é de {area}m²')



if __name__ == "__main__":  
    mostraLinha('Controle de Terrenos')
    time.sleep(2)
    calculoArea(float(input('LARGURA (M):')), float(input('COMPRIMENTO (M):')))
