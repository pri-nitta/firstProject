def perguntar():
    return input("O que deseja realizar?\n" +
                 "1 - Inserir usuário\n" +
                 "2 - Pesquisar usuário\n" +
                 "3 - Excluir usuário\n" +
                 "4 - Listar usuário: ").upper()


# não precisa do retorno, pq é a memória
def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Última estação acessada: ").upper()]


def pesquisar(dicionario):
    nome = input("Digite o login que deseja buscar: ").upper()
    print(dicionario.get(nome))


def excluir(dicionario):
    nome = input("Digite o login que deseja excluir: ").upper()
    print(f"Usuario, {nome} removido com sucesso!")
    dicionario.remove("nome")

