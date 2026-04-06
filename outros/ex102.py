#aplica desconto se a forma de pagamento for em boleto
#calcula o valor das parcelas que a pessoa escolheu

print("Mercadão da alegria")

total_compra = float(input("Por favor, informe o valor total da compra do cliente: "))
forma_pagamento = int (input("Selecione a forma de pagamento: 1 - Boleto ou 2 - Cartão "))

if forma_pagamento == 1:
    total_compra_desconto = total_compra * 0.95
    print(f"O total da compra de R${total_compra:.2f} sofreu um desconto pelo pagamento em boleto. O cliente deverá pagar R${total_compra_desconto:2f}.")
else:
    parcelas = int(input("Informe o número de parcelas desejadas: "))
    valor_parcela = total_compra / parcelas
    print(f"O total da compra de R${total_compra:.2f} será pago em {parcelas} parcelas de R${valor_parcela:.2f}.")
