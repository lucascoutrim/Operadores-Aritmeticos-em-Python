# pede para o usuário digitar uma frase
# upper() transforma tudo em maiúsculo
# strip() remove espaços no começo e no final
frase = str(input('Digite um frase: ')).upper().strip()

#o count conta quantas vezes a letra A aparece na frase
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))

# o find encontra a posição da primeira letra A na frase
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))

#"o rfind começa a contar da direita", encontra a posição da última letra A na frase
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
