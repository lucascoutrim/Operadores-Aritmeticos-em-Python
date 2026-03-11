#pede para o usuário digitar um número!
nome = int(input('Informe um número: '))

#pega o último número (unidade)!
u = nome // 1 % 10

#divide por 10 para remover a unidade e depois pega o resto para achar a dezena!
d = nome // 10 % 10

#divide por 100 para remover unidade e dezena e pega o resto para achar a centena!
c = nome // 100 % 10

#divide por 1000 para pegar o número do milhar!
m = nome // 1000 % 10

#mostra o número digitado!
print('Analisando o número {}'.format(nome))

#mostra cada parte do número!
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))