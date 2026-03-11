nome = str(input('Qual é o seu nome completo? ')).strip()
#strip serve para tirar todos os espaços do começo e do fim!

print('Seu nome tem Coutrim? {}'.format('COUTRIM' in nome.upper()))
#se existir o sobrenome 'Coutrim' dentro da variavel nome o programa vai retornar "true", se não "false"
#coloquei o upper para se caso o usuario digitar coutrim de um forma diferente, o programa vai corrigir transformando tudo em maiusculo primeiro e depois vendo se o sobrenome é coutrim mesmo!
