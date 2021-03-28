# Calculando o bonus do consumo de dados do celular, adaptado ao elif

pontuacao = int(input("Digite sua pontuação mensal: "))

if pontuacao > 1000:
    print("Você ganhou 3gb de bônus!")
elif pontuacao > 500:
    print("Você ganhou 1,5gb de bônus!")
elif pontuacao > 300:
    print("Você ganhou 0,5gb de bônus!")
else:
    print("Infelizmente, você não ganhou nenhum bônus.")
