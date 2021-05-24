from contas import *

opcao = -1


while opcao != 5:
    print("")
    print("Caluladora")
    print("===================")
    print("Digite: (1)Soma (2)Subtração (3)Multiplicação (4)Divisão (5)Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print(somar(int(input("Digite o 1ºn: ")), int(input("Digite o 2ºn "))))
    elif opcao == 2:
        print(subtrair(int(input("Digite o 1ºn: ")), int(input("Digite o 2ºn "))))
    elif opcao == 3:
        print(multiplicar(int(input("Digite o 1ºn: ")), int(input("Digite o 2ºn "))))
    elif opcao == 4:
        n1 = int(input("Digite o 1ºn: "))
        while n1 <= 0:
            n1 = int(input("Digite um dividendo maior que 0! "))
        n2 = int(input("Digite o 2ºn "))
        print(dividir(n1, n2))
