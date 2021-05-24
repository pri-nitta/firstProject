usuarios = {}
emails = ["xpto@email.com", "xkcd@email.com", "abcd@email.com"]

# lista de numeros (usuario) e emails
tupla = list(enumerate(emails))

# acrescenta os dados de nome e nível de acesso aos e-mails
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível de acesso: ")]
    print("--------------------------------")

# print das informações
for chave, dado in usuarios.items():
    print("Usuário:", chave[0])
    print("Email:", chave[1])
    print("Nome:", dado[0])
    print("Nivel:", dado[1])
    print("")
