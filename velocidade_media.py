#Esse programa recebe a distância no tempo e calcula a velocidade média
#Primeiro vamos pedir a distância e o tempo

print("Esse é o calculador de velocidade média da Pri")
distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo percorrido: ")

#Calculo realizado
velocidade_media = float(distancia)/ float(tempo)

#Print do resultado
print("A velocidade média calculada foi de {:.2f} km/h".format(velocidade_media))