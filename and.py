# uma loja que concede desconto nas compras acima de 200 reais e pagamento em dinheiro

valor = float(input("Digite o valor total da compra: "))
pagamento = int(input("Digite a forma de pagamento: 1 - Dinheiro/ 2 - Cartão: "))

if valor > 200 and pagamento == 1:
    valor = valor * 0.95
    print("Ganhou um descontinho de 5%!")
else:
    print("Não ganhou desconto...")

print("O valor total da compra foi {}".format(valor))
