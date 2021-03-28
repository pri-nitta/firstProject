var = input("Qual o tipo da sua assinatura? ")
assinatura = var.upper()
faturamento = float(input("Quanto foi seu faturamento anual? "))

if assinatura == "BASIC":
    bonus = faturamento * 0.3
    print(f"O valor que deverá ser pago é de R${bonus}")

elif assinatura == "SILVER":
    bonus = faturamento * 0.2
    print(f"O valor que deverá ser pago é de R${bonus}")

elif assinatura == "GOLD":
    bonus = faturamento * 0.1
    print(f"O valor que deverá ser pago é de R${bonus}")

elif assinatura == "PLATINUM":
    bonus = faturamento * 0.05
    print(f"O valor que deverá ser pago é de R${bonus}")

else:
    print("Digite um plano válido")

