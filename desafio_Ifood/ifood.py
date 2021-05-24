restaurantes = ["kibon", "makis place", "sukiya", "giraffas", "a feijoada", "Viena", "xpto"]
notas = [4.9, 4.7, 4.6, 4.4, 4.3, 4.8, 5.0]
frete = [6.99, 7.99, 7.99, 5.99, 9.90, 12.49, 0.0]
posicoes = []
y = 0
aux = len(restaurantes)

for x in range(0, 6):
    if notas[x] > notas[x + 1]:
        posicoes.append(restaurantes[x])
    elif notas[x] == notas[x + 1]:
        if frete[x] < frete[x + 1]:
            posicoes.append(restaurantes[x])
        else:
            posicoes.append(restaurantes[x + 1])
    else:
        posicoes.append(restaurantes[x + 1])
    y = y + 1

print(posicoes)
