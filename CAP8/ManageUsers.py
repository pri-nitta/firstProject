from CAP8.Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
    if opcao == "1":
        inserir(usuarios)
    elif opcao == "2":
        pesquisar(usuarios)
    elif opcao == "3":
        excluir(usuarios)
    opcao = perguntar()
