def somar():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print(a + b)

somar()

#Usando parâmetros
def somar2(c, d):
    total = c + d
    print(total)

v1 = float(input("Digite o 1º num: "))
v2 = float(input("Digite o 2º num: "))
somar2(v1, v2)

#passando diretamente parâmetros na função
somar2(54,96)

#usando return
def soma3(x,y):
    total2 = x + y
    return (total2)

print("==============================")
print(soma3(159,753))