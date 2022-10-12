import math

print('exercicio 017 mostrar comprimento hipotenusa a')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co**2)+(ca**2)
re = math.sqrt(hi)
print('O comprimento da hipotenusa é {:.2f}'.format(re))


print('exercicio 017 mostrar comprimento hipotenusa b')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.sqrt(co**2+ca**2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))


print('exercicio 017 mostrar comprimento hipotenusa c')
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
