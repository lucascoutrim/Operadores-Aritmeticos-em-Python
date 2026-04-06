
#Cadastro para saber se você pode ou não doar sangue!

print("Cadastro de doadores de sangue!\n")
nome = input("Por favor, informe o seu nome completo: ")
peso = float (input("Por favor, informe o seu peso em Kg: "))
altura = int(input("Por favor, informe a sua altura em cm: "))
ano_nascimento = int(input("Por favor, informe o seu ano de nascimento: "))

idade = 2026 - ano_nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >=16

texto_saida = f"\tNOME: {nome}\n\tPESO: {peso} kg\n\tALTURA: {altura}cm\n\tIDADE: {idade} anos\n\tTEM PESO MINIMO PARA DOAR: {tem_peso_minimo}\n\tTEM IDADE MINIMA PARA DOAR: {tem_idade_minima}"

print(texto_saida)