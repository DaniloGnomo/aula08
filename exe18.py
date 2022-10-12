import math
import random


print('exercicio 018 ler angulo mostrar seno cosseno etangente')

ang = float(input('Digite o valor do angulo: '))
se = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O seno de {} é: {:.2f}\n'
      'O cosseno de {} é: {:.2f}\n'
      'A tangente de {} é: {:.2f}'.format(ang, se, ang, co, ang, tg))
