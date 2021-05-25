# informar o caminho e o nome do arquivo, modo que vai abrir o arquivo
arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo! Ai que festa!")

arquivo.close()

# automaticamente fecha o arquivo, "w" cria um novo arquivo, abrir com "A" ele insere novas infos
with open("segundo_arquivo.txt", "w") as arquivo1:
    arquivo1.write("\nHakuna Matata!")

with open("terceiro_arquivo.txt", "a") as arquivo2:
    arquivo2.write("Desde o dia em que ao mundo chegamos")
    arquivo2.write("\nCaminhamos ao rumo do sol")
    arquivo2.write("\nHa mais coisas pra ver")
    arquivo2.write("\nMais que a imaginacao")
    arquivo2.write("\nMuito mais que o tempo permitir")

    # recuperar o arquivo
with open("terceiro_arquivo.txt", "r") as arquivo2:
    conteudo = arquivo2.read()
    print(conteudo)
