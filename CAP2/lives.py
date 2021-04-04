print("Gostariamos de saber qual o melhor dia para fazer as lives. \nCaso haja um empate, os alunos deverão votar novamente.")

print("--------------------------------------------")
segunda = int(input("Digite a quantidade de votos recebidos para segunda-feira: "))
terca = int(input("Digite a quantidade de votos recebidos para terça-feira: "))
quarta = int(input("Digite a quantidade de votos recebidos para quarta-feira: "))
quinta = int(input("Digite a quantidade de votos recebidos para quinta-feira: "))
sexta = int(input("Digite a quantidade de votos recebidos para sexta-feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    resultado: str = ("segunda-feira")

elif terca > quarta and terca > quinta and terca > sexta and terca > segunda:
    resultado: str = ("terça-feira")

elif quarta > quinta and quarta > sexta and quarta > segunda and quarta > terca:
    resultado: str = ("quarta-feira")

elif quinta > quarta and quinta > sexta and quinta > segunda and quinta > terca:
    resultado: str = ("quinta-feira")

elif sexta > quinta and sexta > quarta and sexta > segunda and sexta > terca:
    resultado: str = ("sexta-feira")

else:
    print("Houve um empate, vote de novo!")

print(f"O dia mais votado foi: {resultado}")
