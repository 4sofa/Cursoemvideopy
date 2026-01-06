# Crie um programa que leia duas notas de um aluno
nota1 = float(input('Nota primeiro trimestre: '))
nota2 = float(input('Nota segundo trimestre: '))
media = (nota1 + nota2)/2
if media >= 7.00:
    print('\033[32mAPROVADO-APROVADO-\033[m'*5)
    print(' '*15, '\033[32mSua média foi {:.1f}, você foi aprovado, Parabens!\033[m'.format(media))
    print('\033[32mAPROVADO-APROVADO-\033[m'*5)

elif 5.0 <= media <= 6.9:
    print('\033[33mRECUPERAÇÃO-\033[m'*6)
    print(' '*12, '\033[33mSua média foi {:.1f}, você está de recuperação!\033[m'.format(media))
    print('\033[33mRECUPERAÇÃO-\033[m'*6)

elif 0 <= media < 5:
    print('\033[31mREPROVADO-'*8)
    print(' '*14, '\033[31mSua média foi {:.1f}, você foi REPROVADO!\033[m'.format(media))
    print('\033[31mREPROVADO-'*8)
else:
    print('\033[31mERROR-ERROR-\033[m'*5)
    print(' '*18, '\033[31mComo você fez isso?\033[m')
    print('\033[31mERROR-ERROR-\033[m'*5)
