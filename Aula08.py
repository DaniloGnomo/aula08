import math
import random
import playsound


print('exercicio 016 mostrar numero inteiro a')

num = float(input('Digite um numero Real Qualquer: '))
print('{}'.format(int(num)))


print('exercicio 016 mostrar numero inteiro b')

num = float(input('Digite um numero Real Qualquer: '))
print('{}'.format(math.trunc(num)))


print('exercicio 017 mostrar comprimento hipotenusa a')

co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
hi = (co**2)+(ca**2)
re = math.sqrt(hi)
print('O comprimento da hipotenusa é {:.2f}'.format(re))


print('exercicio 017 mostrar comprimento hipotenusa b')

co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
hi = math.sqrt(co**2+ca**2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))


print('exercicio 018 ler angulo mostrar seno cosseno etangente')

ang = int(input('Digite o valor do angulo: '))
se = math.sin(ang)
co = math.cos(ang)
tg = math.tan(ang)
print('O seno de {} é: {:.2f}\n'
      'O cosseno de {} é: {:.2f}\n'
      'A tangente de {} é: {:.2f}'.format(ang, se, ang, co, ang, tg))


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


print('Exercicio 020 lista aleatoria')
au = input('Digite nome do primeiro aluno: ')
ad = input('Digite nome do primeiro aluno: ')
at = input('Digite nome do primeiro aluno: ')
aq = input('Digite nome do primeiro aluno: ')
al = [au, ad, at, aq]
random.shuffle(al)
print('A nova sequencia de alunos é: {}'.format(al))



