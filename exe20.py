import math
import random

print('Exercicio 020 lista aleatoria')
au = input('Digite nome do primeiro aluno: ')
ad = input('Digite nome do segundo aluno: ')
at = input('Digite nome do terceiro aluno: ')
aq = input('Digite nome do quarto aluno: ')
al = [au, ad, at, aq]
random.shuffle(al)
print('A lista de apresentação de alunos é: {}'.format(al))
