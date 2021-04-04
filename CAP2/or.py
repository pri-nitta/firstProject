# O seu crush só ficará com você se você estiver de meias laranjas ou azuis!

nome = input("Qual seu nome? ")
crush = input("Qual o nome do seu crush? ")
meia = input("Você está de meias? S/N ")

if meia == "S" or meia == "s":
    cor = input("Qual a cor da sua meia? ")
    if cor == "Laranja" or cor == "laranja" or cor == "Azul" or cor == "azul":
        print("Temos um match! <3")
    else:
        print("Meia de cor errada! :(")
else:
    print(f"Acho q não rolou {nome}... {crush} não está afim.")
