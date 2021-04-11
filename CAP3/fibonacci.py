# Uma grande empresa de jogos está querendo tornar seus games mais desafiadores.
# Por isso ela contratou você para desenvolver um algoritmo que será aplicado futuramente em diversos outros games:
# o algoritmo da sorte de Fibonnaci.
# A ideia dessa empresa, é claro, é fazer com que seja mais difícil os jogadores terem sucesso nas ações
# que realizam nos games. Por isso o seu algoritmo deverá funcionar da seguinte forma:
# o usuário deve digitar um valor numérico inteiro e o algoritmo deverá verificar se esse valor encontra-se na
# sequência de Fibonnaci. Caso o número esteja na sequência, o algoritmo deve exibir a mensagem “Ação bem sucedida!”
# e, caso não esteja, deve exibir a mensagem “A ação falhou...”.
# A sequência de Fibonacci é muito simples e possui uma lógica de fácil compreensão: ela se inicia em 1
# e cada novo elemento da sequência é a soma entre os dois elementos anteriores. Portanto: 1, 1, 2, 3, 5, 8, 13, 21,
# e assim por diante.
# Logo, se o usuário digitar o número 55 o programa deverá informar que a ação foi bem sucedida,
# afinal 55 está entre os números da sequência. Mas se o usuário digitar o número 6, por exemplo,
# a ação não será bem sucedida, pois o número 6 não está na sequência.

numero = int(input("Digite um número: "))
a = 0
b = 1
soma = 0

while soma < numero:
    soma = a + b
    a = b
    b = soma

if soma == numero:
    print("Ação bem sucedida")
else:
    print("A ação falhou...")