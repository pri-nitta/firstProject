num = int(input("Digite o número da tabuada: "))

for x in range(1, 11):
    print(f"{x} x {num} = {x*num}")

#não precisa da variável contadora, já acrescenta um número a cada loop.
#para definir o inicio, basta colocar o número e uma vírgula

#exibir apenas números impares
for x in range(1, 1001, 2):
    print(x)

#exibir apenas números pares
for x in range(2, 1001, 2):
    print(x)