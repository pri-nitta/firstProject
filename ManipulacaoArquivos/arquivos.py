import json

# ler o arq json
with open("bd.json", "r") as arq_json:
    # carrega a informação em um dicionário
    dic = json.load(arq_json)
    for chave, dados in dic.items():
        print(chave + " " + str(dados))

dicionario = {
    "ELSA": ["FROZEN", "BRANCO", "RAINHA"],
    "ANA": ["FROZEN", "LARANJA", "PRINCESA"],
    "ALADDIN": ["ALADDIN", "PRETO", "HEROI"],
    "JASMINE": ["ALADDIN", "PRETO", "PRINCESA EMPODERADA"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)
