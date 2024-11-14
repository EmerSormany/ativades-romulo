from random import randint
MAX, MIN = 100, 0
acertou = False
numero_sortudo = randint(MIN, MAX)
tentativas = 0
MAX_TENTATIVAS = 5
difculdade = input("""
    Escolha sua difuldade:
    Digite 1 para fácil, 2 para médio e 3 para difícil:   
""")

match difculdade:
    case '1':
        MAX_TENTATIVAS = 10
    case '3':
        MAX_TENTATIVAS = 3


while not acertou and tentativas < MAX_TENTATIVAS:
    num_selecionado = int(input("Digite um número: "))
    if numero_sortudo > num_selecionado:
        print("O número sorteado é maior!")
    elif numero_sortudo < num_selecionado:
        print("O número sorteado é menor!")
    else:
        print("Acertou, miseravi!")
        acertou = True
    tentativas += 1

if acertou:
    print(f"Parabéns, você acertou restando {MAX_TENTATIVAS - tentativas} tentativas.")
    print(f'Número sortudo {numero_sortudo}')
else:
    print("Você gastou todas as tentativas.")
