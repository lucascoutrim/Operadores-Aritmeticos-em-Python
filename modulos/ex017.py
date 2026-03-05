#importamos a biblioteca math, e usamos o comando sqrt para calcular a raiz quadrada!

#from math import sqrt(qualquer função que você quizer! use vírgula se quiser mais de uma! )
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:2f}!'.format(num, raiz))
#mostra a raiz quadrada do valor digitado!

#comando ceil serve para arredondar para cima!
#print('A raiz de {} é igual a {:2f}!'.format(num, math.ceil(raiz)))

#comando floor serve para arredondar para baixo!
#print('A raiz de {} é igual a {:2f}!'.format(num, math.floor(raiz)))