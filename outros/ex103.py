# Sistema que verifica o limite de bagagem por tipo de cliente e informa se há excesso a pagar
tipo_cliente = input("Por favor, informe o tipo do cliente: PREMIUM, GOLD OU REGULAR: ".upper())
peso_bagagem = float(input("Informe o peso da bagagem que o cliente deseja despachar: "))

if tipo_cliente.upper() == "PREMIUM":

    if peso_bagagem <= 32:
        print(f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido! Não é necessário pagar nenhum valor para despachalá!")
    else:
        peso_excedente = peso_bagagem - 32
        print(f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 32kg. A bagagem atual excede este peso em {peso_excedente}kg. Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional! ")

elif tipo_cliente.upper() == "GOLD":

    if peso_bagagem <= 28:
        print(f"Cliente {tipo_cliente}, sua bagagem está dentro do limite permitido! Não é necessário pagar nenhum valor para despachá-la!")
    else:
        peso_excedente = peso_bagagem - 28
        print(f"Os clientes {tipo_cliente} têm direito a despacharem bagagens de até 28kg. A bagagem atual excede este peso em {peso_excedente}kg. Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional!")

else:
    print(f"Os clientes {tipo_cliente} não tem direito à bagagem gratuita. Favor dirigir-se ao balcão de cobranças para realizar o pagamento pela bagagem!.")
