#testes condicionais compostos

aluno = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade de {}: ".format(aluno)))

if idade < 18:
    print("Aluno menor de idade, consulte os responsáveis!")
else:
    print("Aluno maior de idade, cadastro efetuado com sucesso.")