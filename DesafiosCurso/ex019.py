import random
alunos = input('Digite o nome do aluno: ').split(',')
print('O aluno escolhido foi: {}!'.format(random.choice(alunos)))
