#Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde
# as crianças aprendam a controlar os seus gastos. Como forma de validar um protótipo,
# foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES
# financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.
# Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.

transacoes = int(input("Digite quantas transações foram feitas hoje: "))
i = 1
total = 0.0
while i <= transacoes:
    valor = float(input(f"Digite o valor da {i}ª transação: "))
    i = i + 1
    total = (total + valor)

print("==========================================================")
print(f"O valor total das {transacoes} transações foi de: {total}")
print(f"A média do valor de cada transação foi de: {total/ transacoes}")