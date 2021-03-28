# O seu crush só ficará com você se você estiver de meias laranjas ou azuis!

nome = input("Qual seu nome? ")
crush = input("Qual o nome do seu crush? ")
meia = input("Você está de meias? S/N ")

if meia == "S" or "s":
    cor = input("Qual a cor da sua meia? ")
    if cor == "Laranja" or "laranja" or "Azul" or "azul":
        print("Temos um match! <3")
    else:
        print("Meia de cor errada! :(")
else:
    print("Acho q não rolou {}... {} não está afim.".format(nome, crush))
