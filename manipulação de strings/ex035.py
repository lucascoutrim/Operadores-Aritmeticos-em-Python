nome = str(input('Digite seu nome completo: ')).strip()
#strip serve para tirar todos os espaços do começo e do fim!

print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}!'.format(nome.upper()))
#vai deixar o nome com todas as letras maiusculas!

print('Seu nome em minúsculas é {}!'.format(nome.lower()))
#vai deixar o nome com todas as letras minusculas!

print('Seu nome tem ao todo {} letras!'.format(len(nome) - nome.count(' ')))
#conta todas as letras do seu nome!

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras!'.format(separa[0], len(separa[0])))
#a cada espaço o split cria uma lista, e o len conta quantos caracteres existem!
#o zero dentro dos [] significa qual das listas eu quero que o split separou, no caso eu quis a 0 porque era o primeiro nome!