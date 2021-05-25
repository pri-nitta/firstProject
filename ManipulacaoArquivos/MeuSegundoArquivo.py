with open("terceiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)