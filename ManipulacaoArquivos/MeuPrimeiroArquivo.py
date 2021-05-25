# informar o caminho e o nome do arquivo, modo que vai abrir o arquivo
arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo! Ai que festa!")

arquivo.close()

# automaticamente fecha o arquivo, "w" cria um novo arquivo, abrir com "A" ele insere novas infos
with open("segundo_arquivo.txt", "w") as arquivo:
    arquivo.write("\nHakuna Matata!")

with open("terceiro_arquivo.txt", "a") as arquivo:
    arquivo.write("Desde o dia em que ao mundo chegamos")
    arquivo.write("\nCaminhamos ao rumo do sol")
    arquivo.write("\nHa mais coisas pra ver")
    arquivo.write("\nMais que a imaginacao")
    arquivo.write("\nMuito mais que o tempo permitir")