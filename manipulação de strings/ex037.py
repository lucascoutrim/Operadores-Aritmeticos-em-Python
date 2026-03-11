cid = str(input('Em que cidade você nasceu? ')).strip()
#strip serve para tirar todos os espaços do começo e do fim!

print (cid[0:5].upper() == 'SANTO')
#santo só pode haver 5 letras, por isso colocamos o cid[0:5]
# == serve para dizer de cid é igual a SANTO!
#o upper serve para que se o usuario digitar santo de uma forma diferente, o upper vai transformar tudo em maiusculo!