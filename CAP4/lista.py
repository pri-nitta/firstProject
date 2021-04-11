lista = ["guitarra", "violão", "violino", "flauta"]
print(lista)

# adicionar itens
lista.append("bateria")
print(lista)
lista.append(input("Digite o novo instrumento: "))
print(lista)

# colocar o valor em um lugar específico
lista.insert(0, "baixo")
print(lista)

# remover o último elemento da lista
lista.pop()
print(lista)

# remove um item específico
# caso o item não seja encontrado, ele gera um erro
lista.remove("bateria")
print(lista)

# retorna o tamanho da lista
print(len(lista))

# saber a repetição de itens
print(lista.count("guitarra"))

#ordenar a lista (ordem alfabética)
lista.sort()
print(lista)

#ordenar a lista em ordem contrária, inverter sem ser alfabética.
lista.reverse()
print(lista)