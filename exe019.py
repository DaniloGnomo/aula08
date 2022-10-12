import math
import random

print('Exercicio 019 sortear numero')
na = int(input('Numero de alunos na sala: '))
num = random.randint(1, na)
print('O numero do aluno sorteado foi: ', num)

print('Exercicio 019 sortear nome aluno')
au = input('Digite nome do primeiro aluno: ')
ad = input('Digite nome do primeiro aluno: ')
at = input('Digite nome do primeiro aluno: ')
aq = input('Digite nome do primeiro aluno: ')
al = [au, ad, at, aq]
print('O aluno sorteado foi: {}'.format(random.choice(al)))
