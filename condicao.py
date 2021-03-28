funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário de {}: ".format(funcionario)))

if salario < 0:
    salario = salario * -1
    print("O salário digitado foi negativo, portanto o corrigimos")

print("-------------------------------------------------")
print("O salário de {} é {}".format(funcionario, salario))