# Verificação de Ano Bissexto: Escreva um programa que verifica se um ano fornecido pelo usuário é bissexto ou não.

ano = int(input())

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano é bissexto.")
        else:
            print("Não é bissexto")
    else:
        print("O ano é bissexto")
else:
    print("Não é bissexto.")
    