#pede para o usuário digitar o nome completo e remove espaços no começo e no final
n = str(input('Digite o seu nome inteiro: ')).strip()

#separa o nome em partes usando os espaços e cria uma lista
nome = n.split()

#mensagem de apresentação
print('Prazer em te conhecer!')

#mostra o primeiro nome (posição 0 da lista)
print('Seu primeiro nome é {}'.format(nome[0]))

#len(nome) conta quantos nomes existem na lista
#-1 pega a última posição da lista
print('Seu último nome é {}'.format(nome[len(nome)-1]))