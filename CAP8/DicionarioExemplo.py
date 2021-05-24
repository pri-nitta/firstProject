# sempre colocar a lista ou o dicionario no plural
usuarios = {}

# chave e valor, dentro da palavra tem a definição
usuarios = {"chaves": ["Chaves do 8", "24/05/2021", "Recep_01"],
            "quico": ["Quico das Flores", "20/05/2021", "Raiox_03"]}

# criou um novo registro no dicionário
usuarios["florinda"] = ["Dona Florinda", "24/05/2021", "Raiox_04"]
print(usuarios)

print("---------------")

print(usuarios.get("quico"))
